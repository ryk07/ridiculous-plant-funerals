"""Ridiculous at First Glance, Real by the Second — entry.

Writes one sentence pitching a bizarre startup idea to
/output/entry.txt (or to the path in ENTRY_OUTPUT when set, for
local verification). Pure stdlib, no network, no cwd use.
"""

import os
from pathlib import Path

PITCH = "We hold funerals for dead houseplants — tiny coffin, eulogy, the works — because guilty owners pay for closure, then buy a replacement on the way out."
# 150 characters, one sentence: the bizarre idea (funerals for dead
# houseplants), who pays (guilty owners, for closure), and the turn
# that makes it a real business (they buy a replacement on the way out).
# Byte size is 154: the two em dashes are 3 bytes each in UTF-8, and
# the gate counts characters, not bytes.


def main() -> None:
    text = PITCH
    assert 1 <= len(text) <= 200, f"pitch is {len(text)} chars"
    assert text.strip(), "pitch must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), "pitch must be one sentence"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
