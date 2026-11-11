"""Helpers for the course notebooks: the placement check and the hints.

You never need to edit this file. The notebooks import it like this:

    import sys; sys.path.append(".."); from coursetools import hint

The sys.path line lets the import work whether your notebook runs from the
course folder or from inside a week folder.

The hints are stored in base64 so that you only see one when you choose to
run its cell. The placement answers are stored as fingerprints, so they
cannot be read from here at all.
"""

import base64
import hashlib


def _tidy_week1(value):
    return str(value).strip().strip("'\"").lower()


def _tidy_week2(value):
    return " ".join(str(value).replace(",", " ").strip().strip("'\"").lower().split())


def _tidy_brackets(value):
    text = str(value).lower()
    for ch in "[]()'\",":
        text = text.replace(ch, " ")
    return " ".join(text.split())


_TIDY = {1: _tidy_week1, 2: _tidy_week2, 3: _tidy_brackets, 4: _tidy_brackets, 5: _tidy_brackets}

# week: (fingerprints of the right answers, explanation shown for a wrong answer)
_PLACEMENT = {1: ({'q1': '8c25cb3686462e9a',
      'q2': '4e07408562bedb8b',
      'q3': '8a199b120cf400d6',
      'q4': '02d20bbd7e394ad5'},
     {'q1': 'input() always hands back a str, never a number.',
      'q2': '7 // 2 is 3. Integer division throws the remainder away.',
      'q3': '7 / 2 is 3.5. A single slash always gives a float.',
      'q4': 'You get "55". Multiplying a string by an int repeats the string.',
      'q5': 'An f-string needs an f before the quote: print(f"Total: {total}")'}),
 2: ({'q1': '7413995fa9130ef2',
      'q2': '3e23e8160039594a',
      'q3': '4e07408562bedb8b',
      'q4': '4a44dc15364204a8',
      'q5': '0a7aacae9b43f934'},
     {'q1': 'range(2, 8, 2) starts at 2, goes up in 2s, and stops BEFORE 8: 2 4 6',
      'q2': '7 is not even, so the first test fails. The elif is True, so it prints B.',
      'q3': 'n goes 10, 5, 2, 1. The body runs three times, then 1 > 1 is False.',
      'q4': 'range(1, 5) is 1, 2, 3, 4, and they add up to 10.',
      'q5': "continue skips the print for both o's, leaving lp."}),
 3: ({'q1': '6b51d431df5d7f14',
      'q2': '140bedbf9c3f6d56',
      'q3': '7902699be42c8a8e',
      'q4': 'ef2d127de37b942b',
      'q5': '4e07408562bedb8b'},
     {'q1': 'double(3) is 6, and double(6) is 12.',
      'q2': 'greet prints but returns nothing, so result is None.',
      'q3': 'floor rounds DOWN to the whole number below: 7.',
      'q4': 'The x inside change() is a separate, local variable. The outer x is still 5.',
      'q5': 'total gives 6, and 6 // 2 is 3.'}),
 4: ({'q1': '2c624232cdd22177',
      'q2': '535fa30d7e25dd8a',
      'q3': '488a18d5567cf130',
      'q4': '4e07408562bedb8b',
      'q5': '4e07408562bedb8b'},
     {'q1': 'Positions start at 0, so nums[1] is the second item: 8.',
      'q2': '-1 means the last item: 23.',
      'q3': "append adds 'd' to the end, pop(0) removes 'a' from the front: ['b', 'c', 'd'].",
      'q4': 'grid[1] is the row [3, 4], and [0] is its first item: 3.',
      'q5': '15, 16 and 23 are over 10, so 3.'}),
 5: ({'q1': 'a50aba76697ec0b5',
      'q2': '32809fe64114f9d6',
      'q3': '47d8a4a86c7433e2',
      'q4': 'b1a812dda513c887',
      'q5': '4e07408562bedb8b'},
     {'q1': 'int() only takes whole numbers, so "12.5" gives a ValueError. float("12.5") would '
            'work.',
      'q2': 'The positions are 0, 1 and 2, so [3] is past the end: IndexError.',
      'q3': 'The division fails, so print("A") never runs. except prints B, then the program '
            'carries on to C.',
      'q4': 'A dictionary key that is not there gives a KeyError.',
      'q5': 'abc fails int(), -5 fails the if, 7 is accepted: three times.'})}

_HINTS = {(1, 'Core 1'): 'Y2Vsc2l1cyAgICA8LSBhc2sgdGhlIHVzZXIsIGFuZCB0dXJuIHRoZSBhbnN3ZXIgaW50byBhIGZsb2F0CmZhaHJlbmhlaXQgPC0gY2Vsc2l1cyAqIDkgLyA1ICsgMzIKcHJpbnQgYm90aCwgb25lIGRlY2ltYWwgcGxhY2UgZWFjaAoKVGhlIGtleSBsaW5lOgogICAgY2Vsc2l1cyA9IGZsb2F0KGlucHV0KCJFbnRlciBhIHRlbXBlcmF0dXJlIGluIENlbHNpdXM6ICIpKQoKT25lIGRlY2ltYWwgcGxhY2UgaW4gYW4gZi1zdHJpbmc6ICB7ZmFocmVuaGVpdDouMWZ9',
 (1, 'Core 2'): 'dG90YWwgPC0gYWNhZGVtaWMgKyBzcG9ydCArIG11c2ljCnBlcl9wdXBpbCA8LSB0b3RhbCAvIHB1cGlscwpwcmludCB0aGUgdGl0bGUgbGluZQpwcmludCBvbmUgbGluZSBwZXIgZmlndXJlLCBlYWNoIG9uZSBhbiBmLXN0cmluZwoKVGhlIGZpcnN0IHR3byBsaW5lczoKICAgIHByaW50KGYiSG91c2UgcmVwb3J0OiB7aG91c2V9LCB7dGVybX0iKQogICAgcHJpbnQoZiIgIEFjYWRlbWljIHBvaW50czoge2FjYWRlbWljOj40fSIpCgo6PjQgcmlnaHQtYWxpZ25zIGEgbnVtYmVyIGluIDQgc3BhY2VzLCB3aGljaCBsaW5lcyB0aGUgY29sdW1uIHVwLgpPbmUgZGVjaW1hbCBwbGFjZSBpcyA6LjFm',
 (1, 'Core 3'): 'dG90YWwgICAgICAgPC0gYXNrIHRoZSB1c2VyLCBhcyBhIGZsb2F0CnRvdGFsX3BlbmNlIDwtIHJvdW5kKHRvdGFsICogMTAwKQplYWNoX3BlbmNlICA8LSB0b3RhbF9wZW5jZSAvLyAzCmxlZnRfb3ZlciAgIDwtIHRvdGFsX3BlbmNlICUgMwpwcmludCBlYWNoX3BlbmNlIC8gMTAwIHRvIHR3byBkZWNpbWFsIHBsYWNlcywgdGhlbiBsZWZ0X292ZXIKClVzZSByb3VuZCgpLCBub3QgaW50KCkuIEluc2lkZSB0aGUgY29tcHV0ZXIgMTkuOTkgKiAxMDAgaXMKMTk5OC45OTk5OTk5OTk5OTk4LCBhbmQgaW50KCkgd291bGQgY2hvcCB0aGF0IHRvIDE5OTgu',
 (1, 'Fast Track 1'): 'Y29weSB0aGUgdGhyZWUgbGluZXMgb2YgY2Vsc2l1c190b19mYWhyZW5oZWl0CmNoYW5nZSB0aGUgbmFtZSwgdGhlIHBhcmFtZXRlciBhbmQgdGhlIGRvY3N0cmluZwpyZXR1cm4gKGZhaHJlbmhlaXQgLSAzMikgKiA1IC8gOQoKdG8gdGVzdDogIHByaW50KGZhaHJlbmhlaXRfdG9fY2Vsc2l1cygyMTIpKQ==',
 (1, 'Fast Track 2'): 'cmVzdWx0IDwtIGVtcHR5IHN0cmluZwpmb3IgZWFjaCB3b3JkIGluIGZ1bGxfbmFtZS5zcGxpdCgpOgogICAgYWRkIHRoZSB3b3JkJ3MgZmlyc3QgbGV0dGVyLCBpbiBjYXBpdGFscywgdGhlbiAiLiIKcmV0dXJuIHJlc3VsdAoKc3BsaXQoKSB3aXRoIG5vdGhpbmcgaW4gdGhlIGJyYWNrZXRzIGlnbm9yZXMgZXh0cmEgc3BhY2VzLgpzcGxpdCgiICIpIGRvZXMgbm90LCBhbmQgcGFydFswXSBjcmFzaGVzIG9uIHRoZSBlbXB0eSBzdHJpbmdzIGl0IGdpdmVzLg==',
 (1, 'Fast Track 3'): 'd29yayBvdXQgd2hhdCBmIGNhbGN1bGF0ZXMsIGFuZCBuYW1lIGl0IGFmdGVyIHRoYXQKbmFtZSBhLCBiIGFuZCBjIHNvIHRoZSBjYWxsIHJlYWRzIG5hdHVyYWxseQp4IGFuZCB5IG9ubHkgZXhpc3QgdG8gYmUgcmV0dXJuZWQ6IHJldHVybiB0aGUgYW5zd2VyIGRpcmVjdGx5CnRoZSBwcmludCBsaW5lOiBvbmUgZi1zdHJpbmcsIHdpdGggOi4xZiBvbiB0aGUgcmVzdWx0',
 (2, 'Core 1'): 'cGggPC0gYXNrIHRoZSB1c2VyLCBhcyBhIGZsb2F0CmlmIHBoIDwgMzogbGFiZWwgaXMgIlN0cm9uZyBhY2lkIgplbGlmIHBoIDwgNzogbGFiZWwgaXMgIldlYWsgYWNpZCIKZWxpZiBwaCA9PSA3OiBsYWJlbCBpcyAiTmV1dHJhbCIKZWxpZiBwaCA8PSAxMTogbGFiZWwgaXMgIldlYWsgYWxrYWxpIgplbHNlOiBsYWJlbCBpcyAiU3Ryb25nIGFsa2FsaSIKcHJpbnQgcGggYW5kIGxhYmVsCgpUaGUgdGVzdHMgcnVuIHRvcCB0byBib3R0b20sIHNvIGVhY2ggb25lIG9ubHkgbmVlZHMgaXRzIHVwcGVyIGxpbWl0Lg==',
 (2, 'Core 2'): 'Y291bnQgPC0gMTYwMApob3VycyA8LSAwCnByaW50IGhvdXJzIGFuZCBjb3VudAp3aGlsZSBjb3VudCA+PSA1MDoKICAgIGNvdW50IDwtIGNvdW50IC8gMgogICAgaG91cnMgPC0gaG91cnMgKyA2CiAgICBwcmludCBob3VycyBhbmQgY291bnQKcHJpbnQgaG93IG1hbnkgaG91cnMgaXQgdG9vawoKSXQgaXMgYSB3aGlsZSBsb29wIGJlY2F1c2UgeW91IGRvIG5vdCBrbm93IGluIGFkdmFuY2UgaG93IG1hbnkgaGFsdmluZ3MgaXQgbmVlZHMu',
 (2, 'Core 3'): 'ZmFzdGVzdF9zcGVlZCA8LSAwCmZvciBpIGluIHJhbmdlKGxlbihydW5uZXJzKSk6CiAgICBzcGVlZCA8LSAxMDAgLyB0aW1lc1tpXQogICAgcHJpbnQgcnVubmVyc1tpXSBhbmQgc3BlZWQgdG8gMiBkZWNpbWFsIHBsYWNlcwogICAgaWYgc3BlZWQgPiBmYXN0ZXN0X3NwZWVkOgogICAgICAgIGZhc3Rlc3Rfc3BlZWQgPC0gc3BlZWQKICAgICAgICBmYXN0ZXN0X25hbWUgPC0gcnVubmVyc1tpXQpwcmludCBmYXN0ZXN0X25hbWUgYW5kIGZhc3Rlc3Rfc3BlZWQ=',
 (2, 'Fast Track 1'): 'Y29tcGFyaXNvbnMgPC0gMApmb3IgcG9zaXRpb24gaW4gcmFuZ2UobGVuKGl0ZW1zKSk6CiAgICBhZGQgMSB0byBjb21wYXJpc29ucwogICAgaWYgaXRlbXNbcG9zaXRpb25dID09IHRhcmdldDoKICAgICAgICByZXR1cm4gcG9zaXRpb24sIGNvbXBhcmlzb25zCnJldHVybiAtMSwgY29tcGFyaXNvbnM=',
 (2, 'Fast Track 2'): 'bG93IDwtIDAsIGhpZ2ggPC0gbGVuKGl0ZW1zKSAtIDEsIGNvbXBhcmlzb25zIDwtIDAKd2hpbGUgbG93IDw9IGhpZ2g6CiAgICBtaWQgPC0gKGxvdyArIGhpZ2gpIC8vIDIKICAgIGFkZCAxIHRvIGNvbXBhcmlzb25zCiAgICBpZiBpdGVtc1ttaWRdID09IHRhcmdldDogcmV0dXJuIG1pZCwgY29tcGFyaXNvbnMKICAgIGlmIGl0ZW1zW21pZF0gPCB0YXJnZXQ6IGxvdyA8LSBtaWQgKyAxCiAgICBlbHNlOiBoaWdoIDwtIG1pZCAtIDEKcmV0dXJuIC0xLCBjb21wYXJpc29ucwoKRm9yZ2V0IHRoZSArIDEgb3IgLSAxIGFuZCB0aGUgbG9vcCBuZXZlciBlbmRzLiBJZiBhIGNlbGwgcnVucyBmb3JldmVyLApwcmVzcyB0aGUgc3F1YXJlIEludGVycnVwdCBidXR0b24gYXQgdGhlIHRvcCBvZiB0aGUgbm90ZWJvb2su',
 (2, 'Fast Track 3'): 'bG93IDwtIDAKaGlnaCA8LSB0aGUgYmlnZ2VyIG9mIDEgYW5kIG4gICAgICAgIChtYXgoMSwgbikpCnN0ZXBzIDwtIDAKd2hpbGUgaGlnaCAtIGxvdyA+IDAuMDAwMToKICAgIG1pZCA8LSAobG93ICsgaGlnaCkgLyAyCiAgICBhZGQgMSB0byBzdGVwcwogICAgaWYgbWlkICogbWlkIDwgbjogbG93IDwtIG1pZAogICAgZWxzZTogaGlnaCA8LSBtaWQKcmV0dXJuIChsb3cgKyBoaWdoKSAvIDIsIHN0ZXBzCgpVc2UgLyBub3QgLy8sIGJlY2F1c2UgdGhlc2UgYXJlIG5vdCB3aG9sZSBudW1iZXJzLg==',
 (3, 'Core 1'): 'ZGVmIHBlcmNlbnRhZ2VfZXJyb3IobWVhc3VyZWQsIGFjY2VwdGVkKToKICAgIHJldHVybiBhYnMobWVhc3VyZWQgLSBhY2NlcHRlZCkgLyBhY2NlcHRlZCAqIDEwMAoKZXJyb3IgPC0gcGVyY2VudGFnZV9lcnJvcig5LjYsIDkuODEpCnByaW50IGEgc2VudGVuY2Ugd2l0aCBlcnJvciB0byBvbmUgZGVjaW1hbCBwbGFjZToge2Vycm9yOi4xZn0KCmFicygpIHJlbW92ZXMgdGhlIG1pbnVzIHNpZ24sIHNvIG1lYXN1cmluZyB0b28gbG93IGFuZCB0b28gaGlnaCBib3RoIGdpdmUKYSBwb3NpdGl2ZSBlcnJvci4=',
 (3, 'Core 2'): 'ZGVmIGtpbmV0aWNfZW5lcmd5KG1hc3MsIHNwZWVkKToKICAgIHJldHVybiAwLjUgKiBtYXNzICogc3BlZWQgKiogMgoKY2FsbCBpdCBvbmNlIGZvciBlYWNoLCBhbmQgcHJpbnQgdGhlIGFuc3dlciB0byBvbmUgZGVjaW1hbCBwbGFjZQoKKiogbWVhbnMgInRvIHRoZSBwb3dlciBvZiIsIHNvIHNwZWVkICoqIDIgaXMgc3BlZWQgc3F1YXJlZC4=',
 (3, 'Core 3'): 'aW1wb3J0IHJhbmRvbQoKZGVmIGNvdW50X3NpeGVzKHJvbGxzKToKICAgIHNpeGVzIDwtIDAKICAgIHJlcGVhdCByb2xscyB0aW1lczoKICAgICAgICBpZiByYW5kb20ucmFuZGludCgxLCA2KSA9PSA2OiBhZGQgMSB0byBzaXhlcwogICAgcmV0dXJuIHNpeGVzCgpmb3Igcm9sbHMgaW4gWzYwLCA2MDAsIDYwMDAwXToKICAgIHByaW50IHJvbGxzLCBjb3VudF9zaXhlcyhyb2xscykgYW5kIHJvbGxzIC8vIDY=',
 (3, 'Fast Track 1'): 'aW1wb3J0IG1hdGgKCmRlZiBwcm9qZWN0aWxlX3JhbmdlKHNwZWVkLCBhbmdsZT00NSwgZz05LjgxKToKICAgIHJldHVybiBzcGVlZCAqKiAyICogbWF0aC5zaW4obWF0aC5yYWRpYW5zKDIgKiBhbmdsZSkpIC8gZwoKUGFyYW1ldGVycyB3aXRoIGRlZmF1bHRzIG11c3QgY29tZSBhZnRlciB0aGUgb25lcyB3aXRob3V0LgpnPTEuNjIgaW4gYSBjYWxsIGlzIGEga2V5d29yZCBhcmd1bWVudDogaXQgc2tpcHMgYW5nbGUgYW5kIG5hbWVzIGcgZGlyZWN0bHku',
 (3, 'Fast Track 2'): 'SW4gdGhlICUld3JpdGVmaWxlIGNlbGwsIHVuZGVyIGtpbmV0aWNfZW5lcmd5LCBhZGQ6CgpkZWYgd2VpZ2h0KG1hc3MsIGc9OS44MSk6CiAgICAiIiJSZXR1cm4gdGhlIHdlaWdodCBpbiBuZXd0b25zIG9mIGEgbWFzcyBpbiBraWxvZ3JhbXMuIiIiCiAgICByZXR1cm4gbWFzcyAqIGcKClB5dGhvbiBvbmx5IGltcG9ydHMgYSBtb2R1bGUgb25jZS4gQWZ0ZXIgY2hhbmdpbmcgdGhlIGZpbGUsIHRoZQppbXBvcnRsaWIucmVsb2FkIGxpbmUgaW4gdGhlIHNlY29uZCBjZWxsIHBpY2tzIHVwIHlvdXIgY2hhbmdlLg==',
 (3, 'Fast Track 3'): 'aW1wb3J0IHJhbmRvbQoKZGVmIGVzdGltYXRlX3BpKHRocm93cywgc2VlZD1Ob25lKToKICAgIHJhbmRvbS5zZWVkKHNlZWQpCiAgICBoaXRzIDwtIDAKICAgIHJlcGVhdCB0aHJvd3MgdGltZXM6CiAgICAgICAgeCA8LSByYW5kb20ucmFuZG9tKCkgICAgICAgKGEgbnVtYmVyIGZyb20gMCB0byAxKQogICAgICAgIHkgPC0gcmFuZG9tLnJhbmRvbSgpCiAgICAgICAgaWYgeCAqIHggKyB5ICogeSA8PSAxOiBhZGQgMSB0byBoaXRzCiAgICByZXR1cm4gNCAqIGhpdHMgLyB0aHJvd3MKCnJhbmRvbS5zZWVkKE5vbmUpIHNlZWRzIGZyb20gdGhlIGNsb2NrLCBzbyBubyBzZWVkIG1lYW5zIGEgbmV3IGFuc3dlci4=',
 (4, 'Core 1'): 'a2l0LmFwcGVuZCgidGhlcm1vbWV0ZXIiKSwgYW5kIHRoZSBzYW1lIGZvciAic3RvcHdhdGNoIgpraXQucmVtb3ZlKCJidW5zZW4gYnVybmVyIikKa2l0LnNvcnQoKQpmb3IgaSBpbiByYW5nZShsZW4oa2l0KSk6CiAgICBwcmludChmIntpICsgMX0uIHtraXRbaV19IikKcHJpbnQgdGhlIG51bWJlciBvZiBpdGVtcyB3aXRoIGxlbihraXQpCgppICsgMSBiZWNhdXNlIHBvc2l0aW9ucyBzdGFydCBhdCAwIGJ1dCBwZW9wbGUgY291bnQgZnJvbSAxLg==',
 (4, 'Core 2'): 'bWVhbiA8LSBzdW0ocmVhZGluZ3MpIC8gbGVuKHJlYWRpbmdzKQpzcHJlYWQgPC0gbWF4KHJlYWRpbmdzKSAtIG1pbihyZWFkaW5ncykKdW5jZXJ0YWludHkgPC0gc3ByZWFkIC8gMgpwcmludCBhbGwgdGhyZWUgd2l0aCA6LjJmCgpyZWFkaW5ncy5yZW1vdmUoMTYuOSkKdGhlbiB3b3JrIG91dCBhbmQgcHJpbnQgYWxsIHRocmVlIGFnYWluCgpDb3B5aW5nIHRoZSB0aHJlZSBjYWxjdWxhdGlvbiBsaW5lcyBpcyBmaW5lIHRvZGF5LiBOZXh0IHdlZWsgeW91IHdvdWxkCnB1dCB0aGVtIGluIGEgZnVuY3Rpb24u',
 (4, 'Core 3'): 'aW1wb3J0IG1hdGgKdG90YWwgPC0gMApmb3IgbGVuZ3RoLCBwZXJpb2QgaW4gcmVzdWx0czoKICAgIGcgPC0gNCAqIG1hdGgucGkgKiogMiAqIGxlbmd0aCAvIHBlcmlvZCAqKiAyCiAgICBwcmludCBsZW5ndGgsIHBlcmlvZCBhbmQgZywgZWFjaCB0byAyIGRlY2ltYWwgcGxhY2VzCiAgICBhZGQgZyB0byB0b3RhbApwcmludCB0b3RhbCAvIGxlbihyZXN1bHRzKQoKZm9yIGxlbmd0aCwgcGVyaW9kIGluIHJlc3VsdHMgdW5wYWNrcyBlYWNoIHR1cGxlIGludG8gdHdvIHZhcmlhYmxlcy4=',
 (4, 'Fast Track 1'): 'ZGVmIG1vbGFyX21hc3MoZm9ybXVsYSk6CiAgICB0b3RhbCA8LSAwCiAgICBmb3IgZWxlbWVudCBpbiBmb3JtdWxhOgogICAgICAgIHRvdGFsIDwtIHRvdGFsICsgQVRPTUlDX01BU1NbZWxlbWVudF0gKiBmb3JtdWxhW2VsZW1lbnRdCiAgICByZXR1cm4gcm91bmQodG90YWwsIDIpCgpmb3IgZWxlbWVudCwgY291bnQgaW4gZm9ybXVsYS5pdGVtcygpOiBnaXZlcyB5b3UgYm90aCBhdCBvbmNlLg==',
 (4, 'Fast Track 2'): 'cGFpcnMgPC0geyIpIjogIigiLCAiXSI6ICJbIiwgIn0iOiAieyJ9CnN0YWNrIDwtIGVtcHR5IGxpc3QKZm9yIGVhY2ggY2hhcmFjdGVyIGluIHRleHQ6CiAgICBpZiBpdCBpcyBhbiBvcGVuaW5nIGJyYWNrZXQ6IHB1c2ggaXQKICAgIGlmIGl0IGlzIGEgY2xvc2luZyBicmFja2V0OgogICAgICAgIGlmIHRoZSBzdGFjayBpcyBlbXB0eSwgb3IgcG9wKCkgaXMgbm90IGl0cyBwYXJ0bmVyOiByZXR1cm4gRmFsc2UKcmV0dXJuIFRydWUgb25seSBpZiB0aGUgc3RhY2sgaXMgZW1wdHkgYXQgdGhlIGVuZA==',
 (4, 'Fast Track 3'): 'ZnJvbSBjb2xsZWN0aW9ucyBpbXBvcnQgZGVxdWUKcXVldWUgPC0gZGVxdWUoKQpmb3IgZWFjaCBldmVudDoKICAgIGlmIGl0IHN0YXJ0cyB3aXRoICJqb2luIjogcXVldWUuYXBwZW5kKHRoZSBuYW1lIGFmdGVyICJqb2luICIpCiAgICBpZiBpdCBpcyAic2VydmUiOiBwcmludCAiU2VydmVkOiIgYW5kIHF1ZXVlLnBvcGxlZnQoKQpwcmludCBsaXN0KHF1ZXVlKQoKZXZlbnQuc3BsaXQoKSB0dXJucyAiam9pbiBBZGEiIGludG8gWyJqb2luIiwgIkFkYSJdLg==',
 (5, 'Core 1'): 'dHJ5OgogICAgdm9sdGFnZSA8LSBmbG9hdChpbnB1dCguLi4pKQogICAgY3VycmVudCA8LSBmbG9hdChpbnB1dCguLi4pKQogICAgcHJpbnQgdm9sdGFnZSAvIGN1cnJlbnQgdG8gb25lIGRlY2ltYWwgcGxhY2UKZXhjZXB0IFZhbHVlRXJyb3I6CiAgICBwcmludCBhIG1lc3NhZ2UgYWJvdXQgbnVtYmVycyBvbmx5CmV4Y2VwdCBaZXJvRGl2aXNpb25FcnJvcjoKICAgIHByaW50IGEgbWVzc2FnZSBhYm91dCB0aGUgY3VycmVudAoKT25lIHRyeSBjYW4gaGF2ZSBtb3JlIHRoYW4gb25lIGV4Y2VwdC4gUHl0aG9uIHJ1bnMgdGhlIG9uZQp0aGF0IG1hdGNoZXMgdGhlIGVycm9yLg==',
 (5, 'Core 2'): 'd2hpbGUgVHJ1ZToKICAgIHRyeToKICAgICAgICBwaCA8LSBmbG9hdChpbnB1dCguLi4pKQogICAgICAgIGlmIHBoIGlzIGZyb20gMCB0byAxNDogYnJlYWsKICAgICAgICBwcmludCB0aGUgcmFuZ2UgbWVzc2FnZQogICAgZXhjZXB0IFZhbHVlRXJyb3I6CiAgICAgICAgcHJpbnQgdGhlIG51bWJlcnMtb25seSBtZXNzYWdlCnByaW50IHRoZSByZWNvcmRlZCB2YWx1ZQoKMCA8PSBwaCA8PSAxNCBjaGVja3MgYm90aCBlbmRzIGF0IG9uY2Uu',
 (5, 'Core 3'): 'Z29vZCA8LSBlbXB0eSBsaXN0CnJlamVjdGVkIDwtIDAKZm9yIGVudHJ5IGluIGxvZ2dlcjoKICAgIHRyeToKICAgICAgICB2YWx1ZSA8LSBmbG9hdChlbnRyeSkKICAgICAgICBpZiB2YWx1ZSBpcyBmcm9tIC01MCB0byA2MDogYXBwZW5kIGl0IHRvIGdvb2QKICAgICAgICBvdGhlcndpc2U6IGFkZCAxIHRvIHJlamVjdGVkCiAgICBleGNlcHQgVmFsdWVFcnJvcjoKICAgICAgICBhZGQgMSB0byByZWplY3RlZApwcmludCB0aGUgY291bnRzIGFuZCBzdW0oZ29vZCkgLyBsZW4oZ29vZCkKClR3byBraW5kcyBvZiBiYWQ6IG5vdCBhIG51bWJlciAodHJ5IGNhdGNoZXMgaXQpIGFuZCBhIG51bWJlciB0aGF0CmNhbm5vdCBiZSByZWFsIChvbmx5IHlvdXIgaWYgY2F0Y2hlcyBpdCku',
 (5, 'Fast Track 1'): 'ZGVmIGNvbmNlbnRyYXRpb24obW9sZXMsIHZvbHVtZSk6CiAgICBpZiB2b2x1bWUgPD0gMDoKICAgICAgICByYWlzZSBWYWx1ZUVycm9yKCJ2b2x1bWUgbXVzdCBiZSBtb3JlIHRoYW4gemVybyIpCiAgICBpZiBtb2xlcyA8IDA6CiAgICAgICAgcmFpc2UgdGhlIG90aGVyIFZhbHVlRXJyb3IKICAgIHJldHVybiBtb2xlcyAvIHZvbHVtZQoKZm9yIG1vbGVzLCB2b2x1bWUgaW4gc2FtcGxlczoKICAgIHRyeToKICAgICAgICBwcmludCB0aGUgYW5zd2VyCiAgICBleGNlcHQgVmFsdWVFcnJvciBhcyBlcnJvcjoKICAgICAgICBwcmludCBtb2xlcywgdm9sdW1lIGFuZCBlcnJvcgoKImFzIGVycm9yIiBnaXZlcyB5b3UgdGhlIGVycm9yIGl0c2VsZiwgYW5kIHByaW50aW5nIGl0IHNob3dzIGl0cyBtZXNzYWdlLg==',
 (5, 'Fast Track 2'): 'Zm9yIHRleHQgaW4gcmVhZGluZ3M6CiAgICB0cnk6CiAgICAgICAgdmFsdWUgPC0gZmxvYXQodGV4dCkKICAgIGV4Y2VwdCBWYWx1ZUVycm9yOgogICAgICAgIHByaW50KGYiUmVqZWN0ZWQ6ICd7dGV4dH0nIikKICAgIGVsc2U6CiAgICAgICAgYWNjZXB0ZWQuYXBwZW5kKHZhbHVlKQogICAgZmluYWxseToKICAgICAgICBjaGVja2VkIDwtIGNoZWNrZWQgKyAxCgpUaGUgcXVvdGUgbWFya3Mgcm91bmQge3RleHR9IHNob3cgaXQgd2FzIGEgc3RyaW5nIHRoYXQgY291bGQgbm90CmJlIHR1cm5lZCBpbnRvIGEgbnVtYmVyLg==',
 (5, 'Fast Track 3'): 'Z29vZCA8LSAwCnRvdGFsIDwtIDAKbGluZV9udW1iZXIgPC0gMApmb3IgbGluZSBpbiBsaW5lczoKICAgIGxpbmVfbnVtYmVyIDwtIGxpbmVfbnVtYmVyICsgMQogICAgdHJ5OgogICAgICAgIHBhcnRzIDwtIGxpbmUuc3BsaXQoIiwiKQogICAgICAgIHJhaW4gPC0gZmxvYXQocGFydHNbMl0pCiAgICBleGNlcHQgSW5kZXhFcnJvcjoKICAgICAgICBwcmludCB0aGUgbGluZSBudW1iZXIgYW5kICJtaXNzaW5nIGEgZmllbGQiCiAgICBleGNlcHQgVmFsdWVFcnJvcjoKICAgICAgICBwcmludCB0aGUgbGluZSBudW1iZXIgYW5kICJub3QgYSBudW1iZXIiCiAgICBlbHNlOgogICAgICAgIGFkZCAxIHRvIGdvb2QgYW5kIHJhaW4gdG8gdG90YWw='}


def _fingerprint(week, value):
    return hashlib.sha256(_TIDY[week](value).encode()).hexdigest()[:16]


def _week1_q5(answer):
    """Week 1 Q5 asks for code, so it is checked by shape rather than fingerprint."""
    text = str(answer)
    if 'f"' in text or "f'" in text:
        if "{total}" in text:
            return True, ""
        return False, "close. The variable goes inside curly brackets: {total}"
    return False, _PLACEMENT[1][1]["q5"]


def check(week, *answers):
    """Mark the placement check for a week and say which lane to work in."""
    expected, explain = _PLACEMENT[week]
    tidy = _TIDY[week]
    score = 0
    number = 0
    for value in answers:
        number = number + 1
        name = f"q{number}"
        if value is None or tidy(value) == "":
            print(f" - Q{number}: left blank, so no feedback")
            continue
        if week == 1 and name == "q5":
            right, note = _week1_q5(value)
        else:
            right, note = _fingerprint(week, value) == expected[name], explain[name]
        if right:
            score += 1
        else:
            print(f" - Q{number}: {note}")

    print(f"\nScore: {score} out of {len(answers)}\n")
    if score == len(answers):
        print(f"Fast Track this week. Skip the concepts below and open week{week}FastTrack.ipynb.")
    else:
        print(f"Core this week. Work through the concepts below, then open week{week}Core.ipynb.")
        print("Lanes are decided fresh every week, so this says nothing about next week.")


def hint(week, challenge):
    """Print the hint for one challenge, for example hint(3, "Core 1")."""
    print(base64.b64decode(_HINTS[(week, challenge)]).decode())
