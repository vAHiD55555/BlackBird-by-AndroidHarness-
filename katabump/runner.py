#!/usr/bin/env python3
"""BlackBird DataBridge — persistent runner for Katabump server."""

import subprocess
import time
import os
from datetime import datetime

DATA_FILE = os.environ.get("DATA_FILE", "data/market_data.jsonl")
INTERVAL_SECONDS = int(os.environ.get("INTERVAL_SECONDS", "3600"))

LOG_FILE = "logs/server_run.log"

os.makedirs("logs", exist_ok=True)


def log(message):
    timestamp = datetime.now().isoformat()
    line = f"[{timestamp}] {message}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def run_analyze():
    log("Starting analysis...")
    result = subprocess.run(
        ["python3", "analysis/analyze.py", DATA_FILE],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        log(f"Analysis completed: {result.stdout.strip()[:200]}")
    else:
        log(f"Analysis failed: {result.stderr.strip()[:200]}")


def run_compare():
    log("Starting comparison...")
    result = subprocess.run(
        ["python3", "predictions/compare.py", "predictions/predictions.jsonl"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        log(f"Comparison completed:\n{result.stdout.strip()}")
    else:
        log(f"Comparison skipped or failed: {result.stderr.strip()[:200]}")


def main():
    log(f"BlackBird runner started. Interval: {INTERVAL_SECONDS}s")
    log(f"Data file: {DATA_FILE}")

    while True:
        try:
            run_analyze()
            run_compare()
        except Exception as e:
            log(f"Unexpected error: {e}")

        log(f"Sleeping {INTERVAL_SECONDS}s until next run...")
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
