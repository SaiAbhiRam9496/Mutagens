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

### Phase 3 — Hands (mouse/keyboard control) (NEXT)
- [ ] `pyautogui` for UI interaction beyond simple launches
- [ ] `pygetwindow` for window management
- [ ] Expand `KNOWN_APPS` / `KNOWN_SITES` dictionaries

### Phase 4 — Voice
- [ ] Speech-to-text input (`speech_recognition`)
- [ ] Text-to-speech output (`pyttsx3`)

### Phase 5 — Smart fallback (local model)
- [ ] Local model via `transformers` for intent classification only
- [ ] Kicks in only when rule-based parser fails

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

## Notes
- venv is gitignored, recreate it locally with the command above
- No external APIs used — everything runs locally