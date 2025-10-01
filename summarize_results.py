#!/usr/bin/env python3
"""
summarize_results.py
Reads results.log and produces results_summary.md with counts and top exception lines.
Run: python summarize_results.py
"""

from collections import Counter
import re
import os

LOG = "results.log"
OUT = "results_summary.md"

if not os.path.isfile(LOG):
    print(f"Log file not found: {LOG}")
    raise SystemExit(1)

lines = open(LOG, "r", encoding="utf-8", errors="ignore").read().splitlines()

total = 0
ok_count = 0
crash_count = 0
exceptions = []

for ln in lines:
    ln = ln.strip()
    if not ln:
        continue
    total += 1
    if "OK" in ln:
        ok_count += 1
    elif "CRASH" in ln or "Exception" in ln or re.search(r'Exception|Error', ln):
        crash_count += 1
        exceptions.append(ln)

# Get top N unique exception snippets
counter = Counter(exceptions)
top = counter.most_common(10)

with open(OUT, "w", encoding="utf-8") as f:
    f.write("# Results Summary\n\n")
    f.write(f"- Total iterations: {total}\n")
    f.write(f"- OK: {ok_count}\n")
    f.write(f"- CRASH / anomalies: {crash_count}\n\n")
    f.write("## Top exception entries (sampled)\n\n")
    for i, (line, cnt) in enumerate(top, 1):
        # keep lines short
        snippet = (line[:240] + "...") if len(line) > 240 else line
        f.write(f"{i}. `{snippet}` — seen {cnt} times\n\n")
    f.write("## Notes\n\n")
    f.write("- The harness mutates sample inputs; crashes indicate parser exceptions or anomalies worth triage.\n")
    f.write("- To reproduce a specific crash, see `crash_samples/` (if present) for saved mutated inputs.\n")
    f.write("- Do not publish raw exploit payloads publicly; include redacted traces or screenshots instead.\n")

print(f"Wrote summary to {OUT}")
