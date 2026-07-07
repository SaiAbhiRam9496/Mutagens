# parser.py
# Rule-based intent parser: turns raw text into (intent, target, extra)
from difflib import get_close_matches

KNOWN_VERBS = ["open", "close", "focus", "search", "press", "screenshot"]

def fuzzy_match_verb(word):
    matches = get_close_matches(word, KNOWN_VERBS, n=1, cutoff=0.7)
    return matches[0] if matches else None

def parse_command(text):
    text = text.strip().lower()

    # "search X on Y" or "search for X on Y"
    if text.startswith("search"):
        rest = text.replace("search for ", "").replace("search ", "")
        if " on " in rest:
            query, platform = rest.split(" on ", 1)
            return ("search", query.strip(), platform.strip())
        return ("search", rest.strip(), "google")

    # "open the X site" or "open X site" or "open X"
    if text.startswith("open"):
        target = text.replace("open the ", "").replace("open ", "")
        target = target.replace(" site", "").replace(" website", "").replace(" app", "")
        return ("open", target.strip(), None)

    # "close X"
    if text.startswith("close"):
        target = text.replace("close the ", "").replace("close ", "")
        target = target.replace(" app", "")
        return ("close", target.strip(), None)

    # "focus X" or "switch to X"
    if text.startswith("focus") or text.startswith("switch to"):
        target = text.replace("switch to ", "").replace("focus on ", "").replace("focus ", "")
        return ("focus", target.strip(), None)

    # "press ctrl c", "press alt tab", etc.
    if text.startswith("press"):
        keys = text.replace("press ", "").split()
        return ("hotkey", keys, None)

    # Common bare hotkeys people say naturally
    COMMON_HOTKEYS = {
        "alt tab": ["alt", "tab"],
        "control tab": ["ctrl", "tab"],
        "ctrl tab": ["ctrl", "tab"],
        "control c": ["ctrl", "c"],
        "ctrl c": ["ctrl", "c"],
        "control v": ["ctrl", "v"],
        "ctrl v": ["ctrl", "v"],
        "control z": ["ctrl", "z"],
        "ctrl z": ["ctrl", "z"],
        "windows s": ["win", "s"],
        "windows d": ["win", "d"],
        "windows e": ["win", "e"],
    }
    if text in COMMON_HOTKEYS:
        return ("hotkey", COMMON_HOTKEYS[text], None)

    if "voice mode on" in text:
        return ("voice_on", None, None)

    if "voice mode off" in text:
        return ("voice_off", None, None)

    if "screenshot" in text:
        return ("screenshot", None, None)

    # --- FUZZY FALLBACK ---
    # Try to salvage typos/misheard words: check if the first word
    # is *close* to a known verb, even if not exact
    words = text.split()
    if words:
        guessed_verb = fuzzy_match_verb(words[0])
        if guessed_verb:
            remainder = " ".join(words[1:]).strip()
            if guessed_verb == "open":
                return ("open", remainder, None)
            elif guessed_verb == "close":
                return ("close", remainder, None)
            elif guessed_verb == "focus":
                return ("focus", remainder, None)
            elif guessed_verb == "search":
                return ("search", remainder, "google")
            elif guessed_verb == "press":
                return ("hotkey", remainder.split(), None)
            elif guessed_verb == "screenshot":
                return ("screenshot", None, None)

    return ("unknown", text, None)