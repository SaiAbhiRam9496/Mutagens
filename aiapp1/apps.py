# apps.py
# Handles anything related to opening or closing desktop apps

import os
from difflib import get_close_matches

# Known app names and their launch commands
KNOWN_APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "explorer": "explorer",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "vscode": "code",
    "vs code": "code",
    "cmd": "cmd",
    "terminal": "wt",
    "settings": "ms-settings:",
    "task manager": "taskmgr",
    "control panel": "control",
    "file explorer": "explorer",
    "telegram": "Telegram",
}

def open_app(name):
    name = name.strip().lower()
    if not name or len(name) < 2:
        print("That didn't sound like a valid app name — try again.")
        return
    if name not in KNOWN_APPS:
        matches = get_close_matches(name, KNOWN_APPS.keys(), n=1, cutoff=0.5)
        if matches:
            print(f"(Interpreting '{name}' as '{matches[0]}')")
            name = matches[0]
        else:
            print(f"'{name}' isn't a known app. Add it to KNOWN_APPS in apps.py if you want it supported.")
            return
    command = KNOWN_APPS.get(name, name)
    os.system(f"start {command}")
    print(f"Opening {name}")
    
def close_app(name):
    name = name.strip().lower()
    if not name or len(name) < 2:
        print("That didn't sound like a valid app name to close.")
        return
    process_name = KNOWN_APPS.get(name, name)
    result = os.system(f"taskkill /IM {process_name}.exe /F")
    if result != 0:
        print(f"Couldn't close '{name}' — it may not be running.")
    else:
        print(f"Closed {name}")