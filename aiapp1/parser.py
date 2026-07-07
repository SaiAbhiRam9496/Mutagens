# parser.py
# Rule-based intent parser: turns raw text into (intent, target, extra)

def parse_command(text):
    text = text.strip().lower()

    # "search X on Y" or "search for X on Y"
    if text.startswith("search"):
        text = text.replace("search for ", "").replace("search ", "")
        if " on " in text:
            query, platform = text.split(" on ", 1)
            return ("search", query.strip(), platform.strip())
        return ("search", text.strip(), "google")

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

    return ("unknown", text, None)