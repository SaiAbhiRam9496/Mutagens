# apps.py
# Handles anything related to opening or closing desktop apps

import os

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
    """Opens a known app by name."""
    name = name.strip().lower()
    command = KNOWN_APPS.get(name, name)  # fallback: try the raw name
    os.system(f"start {command}")
    print(f"Opening {name}")

def close_app(name):
    """Closes an app by killing its process (best-effort)."""
    name = name.strip().lower()
    process_name = KNOWN_APPS.get(name, name)
    os.system(f"taskkill /IM {process_name}.exe /F")
    print(f"Closing {name}")