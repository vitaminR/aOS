"""Deterministic acceptance checks for task-0303's architecture note."""

from pathlib import Path
import re


NOTE = Path(__file__).with_name("s0-sovereignty-profile.md")
text = NOTE.read_text(encoding="utf-8")

required = [
    "Connected profile",
    "Sovereign / air-gap profile",
    "Zero-network operating contract",
    "What still works",
    "Honest stops",
    "FOUNDER DECISION",
    "ally origin",
    "self-host",
    "license",
    "No production claim",
]

missing = [item for item in required if item.lower() not in text.lower()]
assert not missing, f"missing required content: {missing}"

for level in range(1, 8):
    assert f"**L{level} " in text, f"missing L{level} table row"

table_rows = re.findall(r"^\| \*\*L[1-7] ", text, flags=re.MULTILINE)
assert len(table_rows) == 7, f"expected 7 stratum rows, found {len(table_rows)}"

urls = re.findall(r"https://[^)\s]+", text)
assert len(urls) >= 25, f"expected at least 25 source URLs, found {len(urls)}"

for forbidden in ("DeepSeek", "Qwen", "direct DoD funding recommendation"):
    assert forbidden not in text, f"forbidden content present: {forbidden}"

print(f"PASS task-0303: 7 strata, {len(urls)} source URLs, rails present")
