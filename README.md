# Mutagens

This is where I'm building my own AI assistant — completely from scratch, no external AI APIs, no wrapping someone else's model. The whole point is to actually understand how each piece works: how spoken/typed language turns into a decision, and how that decision turns into a real action on the computer.

## Why from scratch

It would be easy to wire up an API call and call it "AI." That's not the goal here. Every layer — understanding what's being asked, deciding what to do, and executing it — is built and owned end to end, using simple tools first (plain rules, standard libraries) and only reaching for machine learning where it's genuinely needed (a small self-trained classifier as a fallback, not a giant pretrained model).

## Projects

### aiapp1 — Mutagen
The first working version. A local assistant, controlled by text or voice, that can:
- Open and search websites
- Open and close apps
- Switch between open windows
- Send keyboard shortcuts
- Take screenshots
- Listen and respond by voice

It figures out what you mean in three layers: exact command matching first, then fuzzy matching for typos, then a small self-trained model as a last resort for phrasing it hasn't seen before.

Full details, setup instructions, and the complete file breakdown are in [aiapp1/README.md](aiapp1/README.md).

### aiapp2 / aiapp3 — planned
Future iterations, not started yet.

## Philosophy
Build understanding layer by layer. Prefer local, self-built components over external APIs wherever practical — even if it's slower to build, it's actually mine.