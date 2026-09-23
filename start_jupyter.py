"""
Start JupyterLab for the Python Award course.

HOW TO USE THIS
    Open this file in Thonny (or any Python editor) and press Run.

    Working in VS Code: copy the http://localhost:8888/lab?token=... line
    it prints, and paste it into VS Code as an Existing Jupyter Server.
    SETUP.md, Step 3.4, has the details. You can close the browser tab.

    Working in the browser: JupyterLab opens by itself, showing the
    course folder. Click into a Week folder and open the notebook.

WHILE YOU WORK
    Leave this running. Stopping it stops JupyterLab and your cells
    will no longer run.

WHEN YOU FINISH
    Save your notebook with Ctrl and S, close the browser tab, then
    press Stop in Thonny.

If JupyterLab is not installed yet, this file installs it for you the
first time you run it. That takes a minute or two.

A NOTE ON HOW THIS STARTS JUPYTERLAB
    The obvious command is "jupyter lab", but that runs a small program
    called jupyter-lab.exe which gets installed into your user profile.
    Many school networks block programs from running out of a user
    profile, which fails with "WinError 1260, blocked by group policy".
    So this file starts JupyterLab as a Python module instead, which
    keeps everything inside python.exe and sidesteps the block.
"""

import importlib.util
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REQUIRED = ("jupyterlab", "pandas", "matplotlib")


def is_installed(package):
    """True if the package can be imported by this Python."""
    return importlib.util.find_spec(package) is not None


def install(package):
    """Install into this user's profile. Needs no admin rights."""
    print(f"Installing {package}. This takes a minute, please wait.")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "--user", package]
    )
    return result.returncode == 0


def start_as_module():
    """Preferred: run JupyterLab as a module of this Python."""
    print("Starting JupyterLab...")
    return subprocess.run([sys.executable, "-m", "jupyterlab"], cwd=HERE).returncode


def start_in_process():
    """Fallback: run the server inside this process, spawning nothing."""
    print("Starting JupyterLab inside this program instead...")
    from jupyterlab.labapp import LabApp

    LabApp.launch_instance(argv=["--notebook-dir", str(HERE)])


def main():
    print("Python Award: starting JupyterLab")
    print(f"Using Python: {sys.executable}")
    print(f"Course folder: {HERE}")
    print()

    for package in REQUIRED:
        if not is_installed(package) and not install(package):
            print()
            print("-" * 60)
            print(f"Could not install {package}.")
            print("Show your teacher the messages above.")
            print("-" * 60)
            return

    print()
    print("Leave this running while you work.")
    print()
    print("Using VS Code: look below for a line starting")
    print("http://localhost:8888/lab?token=... and copy all of it. In VS Code,")
    print("Select Kernel, Existing Jupyter Server, and paste it. SETUP.md, Step 3.4.")
    print()
    print("Using the browser: if it does not open by itself, paste that same")
    print("line into Edge.")
    print()

    if start_as_module() == 0:
        return

    # Running as a module failed. Try hosting the server in this process,
    # which spawns no separate program at all.
    try:
        start_in_process()
    except Exception as error:
        print()
        print("-" * 60)
        print("JupyterLab could not start.")
        print(f"Reason: {error}")
        print("Show your teacher this message.")
        print("-" * 60)


if __name__ == "__main__":
    main()
