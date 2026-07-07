# websites.py
# Handles anything related to opening or searching websites

import webbrowser

# Known sites and their base URLs
KNOWN_SITES = {
    "youtube": "youtube.com",
    "google": "google.com",
    "github": "github.com",
    "gmail": "mail.google.com",
    "chatgpt": "chat.openai.com",
}

def open_website(name):
    """Opens a known site by name, or treats input as a raw URL."""
    name = name.strip().lower()
    if name in KNOWN_SITES:
        url = KNOWN_SITES[name]
    else:
        url = name  # assume it's already a domain like "example.com"

    if not url.startswith("http"):
        url = "https://" + url

    webbrowser.open(url)
    print(f"Opening {url}")

def search_website(query, platform="google"):
    """Searches a query on a given platform (default: google)."""
    platform = platform.strip().lower()
    query_encoded = query.strip().replace(" ", "+")

    if platform == "google":
        url = f"https://www.google.com/search?q={query_encoded}"
    elif platform == "youtube":
        url = f"https://www.youtube.com/results?search_query={query_encoded}"
    else:
        # fallback: just google it
        url = f"https://www.google.com/search?q={query_encoded}"

    webbrowser.open(url)
    print(f"Searching '{query}' on {platform}")