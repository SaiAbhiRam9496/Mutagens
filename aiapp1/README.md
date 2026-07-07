# Mutagen — aiapp1 (Built From Scratch)

A step-by-step project to build a local, offline-first AI assistant —
no API calls, no cloud brain. Full control, built layer by layer.

## Architecture Plan
Voice/Text Input → Intent Parser → Action Executor → Feedback (voice/text)

## Progress Log

### Phase 1 — Text-only core 
- Built `main.py` with a simple command loop
- Supports:
  - `open <website>` → opens in default browser
  - `open <app>` → launches app via `os.system`
  - `quit` → exits
- Uses only Python standard library (`webbrowser`, `os`) — zero dependencies
- Tested and working: `open youtube.com`, `open notepad`, `open google.com`

### Phase 2 — Modular structure + smarter parsing 
- Split code into separate files by responsibility:
  - `parser.py` — rule-based intent parser (text → intent, target, extra)
  - `websites.py` — known sites dictionary, open/search logic
  - `apps.py` — known apps dictionary, open/close logic
  - `main.py` — input loop, routes parsed intent to the right handler
- New supported patterns:
  - `open <known site>` (e.g. "open youtube")
  - `open the <site> site` / `open <site> website`
  - `search <query>` / `search for <query> on <platform>`
  - `close <app>`
- Tested and working:
  - `open youtube` ✅
  - `search for cats on google` ✅
  - `search python tutorials` ✅
  - Unknown commands correctly fall through to "Sorry, I don't understand that yet." ✅

### Phase 3 — Hands (mouse/keyboard/window control) ✅ DONE
- `hands.py` added:
  - `focus_window()` — switches to an open window by matching title substring
  - `press_hotkey()` — simulates key combos (alt+tab, ctrl+c, etc.)
  - `take_screenshot()` — saves timestamped screenshots to `screenshots/`
- New parser intents: `focus`, `hotkey`, `screenshot`
- Bare hotkey phrases supported ("alt tab", "control c", "windows d") via a lookup table, no need to say "press" explicitly
- Known limitation: `pygetwindow.activate()` occasionally raises a false-positive Windows error even on success — wrapped in try/except to prevent crashes

### Phase 4 — Voice ✅ DONE
- `voice.py` added:
  - `listen()` — mic input via `speech_recognition` (Google Web Speech API, needs internet)
  - `speak()` — offline text-to-speech via `pyttsx3`
- `main.py` now supports a voice/text toggle:
  - Say/type `"voice mode on"` to switch to mic input
  - Say/type `"voice mode off"` to return to typed input
- Expanded quit phrases: `quit`, `exit`, `bye`, `goodbye`, `stop`
- Tested and working: open/search/focus/hotkey commands all functional via voice
- Known limitation: no wake word yet — voice mode listens continuously in a loop once turned on

### Phase 5 — Smart fallback (local model) (NEXT)
- [ ] Local model via `transformers` for intent classification only
- [ ] Kicks in only when rule-based parser fails
- [ ] Consider wake-word detection for hands-free activation

## Project Structure

- aiapp1/
- main.py        → entry point, input loop, routing
- parser.py      → rule-based intent parsing
- websites.py    → website open/search logic
- apps.py        → app open/close logic
- venv/          → local environment (gitignored)

## Setup

- python -m venv venv
- venv\Scripts\Activate.ps1
- python main.py

## Requirements
See `requirements.txt`. Install with:
```
pip install -r requirements.txt
```

## Notes
- venv is gitignored, recreate it locally with the command above
- No external APIs used — everything runs locally