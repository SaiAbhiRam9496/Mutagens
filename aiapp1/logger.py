# logger.py
# Simple command logging for debugging and future training data

import os
from datetime import datetime

LOG_PATH = "log.txt"

def log_command(raw_text, intent, target, success=True):
    os.makedirs(os.path.dirname(LOG_PATH) or ".", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "OK" if success else "FAIL"
    line = f"[{timestamp}] {status} | raw='{raw_text}' | intent={intent} | target={target}\n"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)