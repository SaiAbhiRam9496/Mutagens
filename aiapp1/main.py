# main.py
# Entry point: reads input, parses intent, routes to the right handler
from hands import focus_window
from parser import parse_command
from websites import open_website, search_website, KNOWN_SITES
from apps import open_app, close_app

def route_command(intent, target, extra):
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

    else:
        print("Sorry, I don't understand that yet.")

def main():
    print("Mutagen is running. Type a command (or 'quit' to exit).")
    while True:
        command = input("You: ").strip()
        if command.lower() == "quit":
            break
        intent, target, extra = parse_command(command)
        route_command(intent, target, extra)

if __name__ == "__main__":
    main()