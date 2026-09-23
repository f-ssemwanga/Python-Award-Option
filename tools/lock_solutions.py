"""
Lock a week's model solutions into its challenges notebook.

TEACHER ONLY. Students never need to run this.

    python tools/lock_solutions.py Week1/week1Challenges.ipynb solutions/week1.md

It asks for a passphrase twice, encrypts the markdown file with it, and
writes the result into the notebook cell tagged "locked-solutions". The
plain text solutions live in solutions/, which .gitignore keeps out of the
repository, so only the locked version is ever pushed.

The cell's outputs are cleared every time this runs. That matters: if you
unlock the solutions in your own copy to check them, the revealed text is
saved in the notebook's output. Run this script again before committing
and the output is wiped.

How strong the lock is depends entirely on the passphrase. The notebook
is public, so a student can copy the locked text and try passphrases in a
loop. A four digit PIN has 10,000 possibilities and falls in about an hour
of trying. Three ordinary words picked at random do not.

Standard library only, so it runs on the school machines without pip.
"""

import base64
import getpass
import hashlib
import hmac
import json
import os
import pathlib
import sys
import zlib

ITERATIONS = 300_000
TAG = "locked-solutions"


def normalise(passphrase):
    """Ignore case and stray spaces so students are not caught out by typing."""
    return " ".join(passphrase.lower().split())


def keystream(key, length):
    blocks = (hashlib.sha256(key + i.to_bytes(8, "big")).digest()
              for i in range(length // 32 + 1))
    return b"".join(blocks)[:length]


def lock(text, passphrase):
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac("sha256", normalise(passphrase).encode(),
                              salt, ITERATIONS, dklen=64)
    plain = zlib.compress(text.encode("utf-8"), 9)
    body = bytes(a ^ b for a, b in zip(plain, keystream(key[:32], len(plain))))
    tag = hmac.new(key[32:], salt + body, "sha256").digest()
    return base64.encodebytes(salt + tag + body).decode("ascii")


def unlock(blob, passphrase):
    """Same as the notebook's version. Used here to prove the lock round trips."""
    data = base64.b64decode(blob)
    salt, tag, body = data[:16], data[16:48], data[48:]
    key = hashlib.pbkdf2_hmac("sha256", normalise(passphrase).encode(),
                              salt, ITERATIONS, dklen=64)
    expected = hmac.new(key[32:], salt + body, "sha256").digest()
    if not hmac.compare_digest(tag, expected):
        return None
    plain = bytes(a ^ b for a, b in zip(body, keystream(key[:32], len(body))))
    return zlib.decompress(plain).decode("utf-8")


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    notebook_path = pathlib.Path(sys.argv[1])
    solutions_path = pathlib.Path(sys.argv[2])
    text = solutions_path.read_text(encoding="utf-8")

    passphrase = os.environ.get("SOLUTIONS_PASSPHRASE")
    if not passphrase:
        passphrase = getpass.getpass("Passphrase: ")
        if getpass.getpass("Same again: ") != passphrase:
            print("The two did not match. Nothing was changed.")
            sys.exit(1)
    if len(normalise(passphrase)) < 12:
        print("Warning: short passphrases can be guessed by a loop in minutes.")

    blob = lock(text, passphrase)
    assert unlock(blob, passphrase) == text, "round trip failed"

    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    cells = [c for c in notebook["cells"]
             if TAG in c.get("metadata", {}).get("tags", [])]
    if len(cells) != 1:
        print(f"Expected one cell tagged {TAG!r}, found {len(cells)}.")
        sys.exit(1)

    cell = cells[0]
    source = "".join(cell["source"])
    start = source.index('LOCKED = """') + len('LOCKED = """')
    end = source.index('"""', start)
    source = source[:start] + "\n" + blob + source[end:]
    cell["source"] = source.splitlines(keepends=True)
    cell["outputs"] = []
    cell["execution_count"] = None

    notebook_path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n",
                             encoding="utf-8")
    print(f"Locked {solutions_path} into {notebook_path}.")


if __name__ == "__main__":
    main()
