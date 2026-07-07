\# Mutagens — aiaap1 



A step-by-step project to build a local, offline-first AI assistant —

no API calls, no cloud brain. Full control, built layer by layer.



\## Architecture Plan

Voice/Text Input → Intent Parser → Action Executor → Feedback (voice/text)



\## Progress Log



\### Phase 1 — Text-only core ✅ DONE

\- Built `main.py` with a simple command loop

\- Supports:

&#x20; - `open <website>` → opens in default browser

&#x20; - `open <app>` → launches app via `os.system`

&#x20; - `quit` → exits

\- Uses only Python standard library (`webbrowser`, `os`) — zero dependencies

\- Tested and working: `open youtube.com`, `open notepad`, `open google.com`



\### Phase 2 — Smarter parsing (NEXT)

\- \[ ] Handle flexible phrasing ("open the youtube site", "search X on google")

\- \[ ] Separate website detection from app detection more robustly

\- \[ ] Add "close <app>" support



\### Phase 3 — Hands (mouse/keyboard control)

\- \[ ] `pyautogui` for UI interaction beyond simple launches

\- \[ ] `pygetwindow` for window management



\### Phase 4 — Voice

\- \[ ] Speech-to-text input (`speech\_recognition`)

\- \[ ] Text-to-speech output (`pyttsx3`)



\### Phase 5 — Smart fallback (local model)

\- \[ ] Local model via `transformers` for intent classification only

\- \[ ] Kicks in only when rule-based parser fails



\## Setup

python -m venv venv
venv\Scripts\Activate.ps1
python main.py

## Notes
- venv is gitignored, recreate it locally with the command above
- No external APIs used — everything runs locally

