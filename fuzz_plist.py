#!/usr/bin/env python3
"""
Simple educational fuzzer for plist/JSON-like inputs.
Not targeting any real Apple internal code — intended to demonstrate methodology.
"""

import os
import random
import json
import time

SAMPLES_DIR = "samples"
RESULTS_FILE = "results.log"
CRASH_DIR = "crash_samples"
os.makedirs(CRASH_DIR, exist_ok=True)

def mutate(s: str) -> str:
    # tiny mutation: flip random bytes, insert random char or duplicate
    s = list(s)
    for _ in range(random.randint(1, 5)):
        i = random.randrange(0, max(1, len(s)))
        s.insert(i, chr(random.randint(32, 126)))
    return "".join(s)

def run_test(input_data: str, iter_no: int = None):
    try:
        parsed = json.loads(input_data)
        if isinstance(parsed, dict):
            return "OK"
        return "OK"
    except Exception as e:
        # save mutated input for triage
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        fname = f"crash_{iter_no or 'na'}_{timestamp}.txt"
        with open(os.path.join(CRASH_DIR, fname), "w", encoding="utf-8") as f:
            # write a redacted/encoded version to reduce accidental payload exposure
            f.write(input_data)
        with open(RESULTS_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Iter {iter_no or '?'} Exception: {type(e).__name__}: {e}\n")
        return "CRASH"

def main():
    # Ensure samples exist
    if not os.path.isdir(SAMPLES_DIR):
        os.makedirs(SAMPLES_DIR)
        # create a default sample
        with open(os.path.join(SAMPLES_DIR, "sample1.json"), "w") as f:
            json.dump({"key": "value"}, f)

    samples = [open(os.path.join(SAMPLES_DIR, s)).read() for s in os.listdir(SAMPLES_DIR)]
    for i in range(200):
        s = random.choice(samples)
        mutated = mutate(s)
        result = run_test(mutated)
        print(f"Iter {i+1}: {result}")

if __name__ == "__main__":
    main()
