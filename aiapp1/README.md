# Mutagen — Agent 1 (aiapp1)

Mutagen is a personal AI assistant built entirely from scratch — no external AI APIs, no cloud-based "brain." Everything runs locally on your machine: understanding what you say, deciding what to do, and actually doing it (opening apps, searching the web, controlling windows, even listening and talking back).

This folder (`aiapp1`) is the first working version of Mutagen.

---

## How it works (the pipeline)

```
Your voice or typed text
        ↓
  voice.py (if voice mode) → converts speech to text
        ↓
  parser.py → figures out what you mean
        │
        ├── Step 1: exact rule matching (fast, precise)
        ├── Step 2: fuzzy matching (catches typos/misheard words)
        └── Step 3: trained classifier (catches different phrasing)
        ↓
  main.py → routes the decision to the right file
        ↓
  ┌─────────────┬─────────────┬─────────────┐
  websites.py     apps.py       hands.py
  (open/search    (open/close    (window focus,
   sites)          apps)          hotkeys, screenshots)
        ↓
  voice.py (if voice mode) → speaks confirmation back
        ↓
  logger.py → records what happened for later review
```

Every command you give goes through this same pipeline. The parser tries the cheapest, most reliable method first (exact match), and only falls back to fuzzy matching or the trained model if it has to.

---

## Files and what each one does

| File | What it does |
|---|---|
| `main.py` | The entry point. Runs the main loop, reads your command (typed or spoken), sends it to the parser, and routes the result to the right action. |
| `parser.py` | The "brain" that decides what you meant. Tries rules first, then fuzzy matching, then the trained classifier as a last resort. |
| `websites.py` | Knows how to open and search websites. Has a dictionary of common sites (YouTube, Google, GitHub, etc.). |
| `apps.py` | Knows how to open and close desktop apps. Has a dictionary of common apps (Notepad, Chrome, VS Code, etc.). Validates targets so it won't try to launch garbage. |
| `hands.py` | Direct control over your machine — switching between open windows, sending keyboard shortcuts (like Alt+Tab), and taking screenshots. |
| `voice.py` | Converts your speech to text (listening) and speaks responses back (talking) — fully local text-to-speech, speech recognition uses Google's free API (needs internet). |
| `classifier.py` | Trains and loads a small machine learning model that guesses intent when nothing else matches. |
| `training_data.py` | The example phrases used to teach the classifier. Add more of your own phrasing here to improve accuracy over time. |
| `logger.py` | Writes every command and its result to `log.txt`, for debugging and future training data. |
| `requirements.txt` | The list of Python packages this project needs. |

---

## Setup

**1. Create and activate a virtual environment** (keeps dependencies isolated):
```
python -m venv venv
venv\Scripts\Activate.ps1
```

**2. Install requirements:**
```
pip install -r requirements.txt
```

**3. Run it:**
```
python main.py
```

---

## Basic commands

**Websites:**
- `open youtube`
- `search for cats on google`
- `search python tutorials`

**Apps:**
- `open notepad`
- `close notepad`

**Window control:**
- `focus chrome` / `switch to chrome`
- `alt tab`
- `control c`

**Screenshots:**
- `take a screenshot`

**Voice:**
- `voice mode on` — switches to listening mode. Once on, say **"mutagen"** before every command (e.g. "mutagen open chrome") — this is the wake word, so it doesn't act on background noise or conversation.
- `voice mode off` — switches back to typing.

**Exit:**
- `quit`, `exit`, `bye`, `goodbye`, or `stop`

---

## Tools used (and why)

**Python standard library** (`webbrowser`, `os`, `subprocess`) — handles opening websites and launching apps with zero external dependencies. This is the foundation; no installs needed for basic open/close functionality.

**pyautogui** — simulates mouse and keyboard input (used here for keyboard shortcuts like Alt+Tab). Has a built-in safety feature: moving your mouse to a screen corner aborts any automated action mid-way, in case something goes wrong.

**pygetwindow** — finds and switches between open windows by matching their title text. This is what powers the "focus chrome" / "switch to X" commands.

**Pillow (PIL)** — handles image saving, used by pyautogui for capturing and saving screenshots.

**SpeechRecognition** — converts spoken audio into text. Uses Google's free Web Speech API under the hood, which means it needs an internet connection, but there's no API key or account required.

**pyttsx3** — converts text into spoken audio, fully offline (unlike the speech recognition side, this doesn't need internet). Used for Mutagen's voice responses.

**scikit-learn** — a classical machine learning library (not deep learning). Used here to train a small text classifier from scratch on hand-written example phrases, so Mutagen can guess intent even when the exact wording doesn't match any rule. Specifically uses:
- **TF-IDF Vectorizer** — converts text into numbers based on word importance/frequency, so the model can actually do math on it.
- **Logistic Regression** — a simple, fast classification algorithm that learns to map those numbers to an intent label (open, close, focus, search, etc.).

**joblib** — saves and loads the trained model to/from disk, so it doesn't need to retrain every time the program runs.

---

## Known limitations

- The classifier fallback is only as good as its training data — currently trained on a small hand-written set, so confidence on unusual phrasing can be low. Improves as more examples get added to `training_data.py`.
- Voice recognition needs an internet connection (Google's API).
- Some apps need their exact launch command or full path added to `KNOWN_APPS` in `apps.py` before Mutagen can open them.
- `pygetwindow`'s window activation occasionally throws a harmless false-positive error on Windows — handled internally, doesn't affect functionality.