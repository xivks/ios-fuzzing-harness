# Fuzzing Results Summary

The fuzzing harness executed 200 iterations.

- Majority of runs triggered crashes due to malformed or unexpected input.
- Occasional successful parses (`OK`) were observed at iterations 51, 160, 187.
- Exceptions observed include ValueError, KeyError, and UnicodeDecodeError.
- Results indicate robustness issues in plist parsing that need deeper review.

## Notes
- Crashes are reproducible with randomized malformed inputs.
- Further iteration scaling may expose additional exception types.
- Use `summarize_results.py` for automated statistics on pass/crash ratios.
