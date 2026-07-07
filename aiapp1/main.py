# main.py
# Entry point: reads input (text or voice), parses intent, routes to the right handler

from parser import parse_command
from websites import open_website, search_website, KNOWN_SITES
from apps import open_app, close_app
from hands import focus_window, press_hotkey, take_screenshot
from voice import listen, speak

VOICE_MODE = False  # toggle with "voice mode on" / "voice mode off"

def route_command(intent, target, extra):
    global VOICE_MODE

    if intent == "search":
        search_website(target, extra)

    elif intent == "open":
        if target in KNOWN_SITES or "." in target:
            open_website(target)
        else:
            open_app(target)

    elif intent == "close":
        close_app(target)

    elif intent == "focus":
        focus_window(target)

    elif intent == "hotkey":
        press_hotkey(*target)
        print(f"Pressed: {' + '.join(target)}")

    elif intent == "screenshot":
        path = take_screenshot()
        print(f"Screenshot saved to {path}")

    elif intent == "voice_on":
        VOICE_MODE = True
        print("Voice mode ON")
        speak("Voice mode on")

    elif intent == "voice_off":
        VOICE_MODE = False
        print("Voice mode OFF")

    else:
        print("Sorry, I don't understand that yet.")

def get_command():
    global VOICE_MODE
    if VOICE_MODE:
        text = listen()
        return text if text else ""
    else:
        return input("You: ").strip()

def main():
    print("Mutagen is running. Type 'voice mode on' to switch to voice, or 'quit' to exit.")
    while True:
        command = get_command()
        if not command:
            continue
        if command.lower() in ["quit", "exit", "bye", "goodbye", "stop"]:
            break
        intent, target, extra = parse_command(command)
        route_command(intent, target, extra)

if __name__ == "__main__":
    main()