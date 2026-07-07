import webbrowser
import os

def open_website(url):
    if not url.startswith("http"):
        url = "https://" + url
    webbrowser.open(url)

def open_app(app_name):
    os.system(f"start {app_name}")

def main():
    print("Jarvis-lite is running. Type a command (or 'quit' to exit).")
    while True:
        command = input("You: ").strip().lower()
        if command == "quit":
            break
        elif command.startswith("open "):
            target = command.replace("open ", "").strip()
            if "." in target:
                open_website(target)
            else:
                open_app(target)
        else:
            print("Sorry, I don't understand that yet.")

if __name__ == "__main__":
    main()