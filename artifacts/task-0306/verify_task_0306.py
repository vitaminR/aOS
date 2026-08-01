"""Deterministic acceptance checks for task-0306's pilot plan."""

from pathlib import Path
import re


NOTE = Path(__file__).with_name("90-day-agentic-pilot-plan.md")
text = NOTE.read_text(encoding="utf-8")

metrics = [
    "Cost per successful task",
    "Trace coverage",
    "Evaluation pass rate",
    "Policy denial rate",
    "Approval latency",
    "Budget variance",
]
for metric in metrics:
    assert metric in text, f"missing metric: {metric}"

for phase in range(1, 4):
    assert f"Phase {phase}" in text, f"missing Phase {phase}"

assert text.count("exit criteria") >= 3, "each phase needs exit criteria"
assert text.lower().count("goal") >= 8, "target bands must be labeled goals"
assert "not performance claims" in text.lower(), "performance-claim boundary missing"
assert "FOUNDER DECISION" in text, "founder-decision boundary missing"
assert "protégé/subcontract" in text, "approved contracting lane missing"
assert "authorize a separately scoped production transition" in text

urls = re.findall(r"https://[^)\s]+", text)
assert len(urls) >= 10, f"expected at least 10 source URLs, found {len(urls)}"

metric_rows = re.findall(r"^\| \*\*[1-6]\. ", text, flags=re.MULTILINE)
assert len(metric_rows) == 6, f"expected 6 metric rows, found {len(metric_rows)}"

for forbidden in ("DeepSeek", "Qwen", "FedRAMP compliant", "DoD-funded"):
    assert forbidden not in text, f"forbidden claim present: {forbidden}"

print(f"PASS task-0306: 6 metrics, 3 phases, {len(urls)} source URLs, rails present")
