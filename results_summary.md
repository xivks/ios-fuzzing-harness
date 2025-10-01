# Results Summary

- Total iterations: 203
- OK: 2
- CRASH / anomalies: 199

## Top exception entries (sampled)

1. `[2025-10-02 01:01:59] Crash/Exception: Expecting value: line 1 column 1 (char 0)` — seen 167 times

2. `[2025-10-02 01:01:59] Crash/Exception: Extra data: line 1 column 2 (char 1)` — seen 15 times

3. `[2025-10-02 01:01:59] Crash/Exception: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` — seen 7 times

4. `[2025-10-02 01:01:59] Crash/Exception: Expecting value: line 1 column 2 (char 1)` — seen 3 times

5. `[2025-10-02 01:01:59] Crash/Exception: Extra data: line 1 column 3 (char 2)` — seen 2 times

6. `[2025-09-24 18:05:45] Iter 57: Exception caught: JSONDecodeError: Expecting value at line 1 column 1 (document starts with invalid token)` — seen 1 times

7. `[2025-09-24 18:06:40] Iter 157: Exception caught: ValueError: too many nested structures (depth 1024) — recorded for analysis` — seen 1 times

8. `[2025-10-02 01:01:59] Crash/Exception: Expecting property name enclosed in double quotes: line 2 column 1 (char 2)` — seen 1 times

9. `[2025-10-02 01:01:59] Crash/Exception: Expecting value: line 2 column 1 (char 2)` — seen 1 times

10. `[2025-10-02 01:01:59] Crash/Exception: Invalid control character at: line 1 column 6 (char 5)` — seen 1 times

## Notes

- The harness mutates sample inputs; crashes indicate parser exceptions or anomalies worth triage.
- To reproduce a specific crash, see `crash_samples/` (if present) for saved mutated inputs.
- Do not publish raw exploit payloads publicly; include redacted traces or screenshots instead.
