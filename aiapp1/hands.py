# hands.py
# Direct UI control: mouse, keyboard, window management
import os
import pyautogui
import pygetwindow as gw
import time

pyautogui.FAILSAFE = True  # move mouse to top-left corner to abort a running action

def click_at(x, y):
    pyautogui.click(x, y)

def type_text(text, interval=0.03):
    pyautogui.typewrite(text, interval=interval)

def press_key(key):
    pyautogui.press(key)

from datetime import datetime

SCREENSHOT_DIR = "screenshots"

def take_screenshot():
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    save_path = os.path.join(SCREENSHOT_DIR, filename)
    img = pyautogui.screenshot()
    img.save(save_path)
    return save_path

def focus_window(title_substring):
    """Finds a window whose title contains the given substring and brings it to front."""
    matches = [w for w in gw.getAllTitles() if title_substring.lower() in w.lower()]
    if not matches:
        print(f"No window found matching '{title_substring}'")
        return False
    win = gw.getWindowsWithTitle(matches[0])[0]
    try:
        win.activate()
    except Exception:
        pass  # pygetwindow sometimes raises a false error even on success
    time.sleep(0.3)
    print(f"Switched to: {matches[0]}")
    return True

def list_open_windows():
    titles = [t for t in gw.getAllTitles() if t.strip()]
    return titles

def press_hotkey(*keys):
    pyautogui.hotkey(*keys)