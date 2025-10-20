import os
import json
import time
import random

# === Directories & Files ===
SAMPLES_DIR = "samples"
CRASH_DIR = "crashes"
RESULTS_FILE = "results.log"


def mutate(s: str) -> str:
    """Simple mutator - can be extended for fuzzing"""
    return "".join(s)


def run_test(input_data: str, iter_no: int = None) -> str:
    try:
        parsed = json.loads(input_data)
        if isinstance(parsed, dict):
            return "OK"
        return "OK"
    except Exception as e:
        # Log crash details
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        fname = f"crash_iter{iter_no or 'na'}_{timestamp}.txt"

        # Save crashing input
        os.makedirs(CRASH_DIR, exist_ok=True)
        with open(os.path.join(CRASH_DIR, fname), "w", encoding="utf-8") as f:
            f.write(input_data)

        # Log to results file
        with open(RESULTS_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Iter {iter_no or '?'} "
                    f"Exception: {type(e).__name__}: {e}\n")
        return "CRASH"


def main():
    # Ensure samples folder exists
    if not os.path.isdir(SAMPLES_DIR):
        os.makedirs(SAMPLES_DIR)
        # Create a default sample if missing
        with open(os.path.join(SAMPLES_DIR, "sample1.json"), "w") as f:
            json.dump({"key": "value"}, f)

    # Load all samples
    samples = [open(os.path.join(SAMPLES_DIR, s)).read()
               for s in os.listdir(SAMPLES_DIR)]

    # Run fuzzing loop
    for i in range(200):
        s = random.choice(samples)
        mutated = mutate(s)
        result = run_test(mutated, iter_no=i + 1)
        print(f"Iter {i+1}: {result}")


if __name__ == "__main__":
    main()
