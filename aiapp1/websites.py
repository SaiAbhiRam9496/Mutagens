# websites.py
# Handles anything related to opening or searching websites

import webbrowser
from difflib import get_close_matches

# Known sites and their base URLs
KNOWN_SITES = {
    "youtube": "youtube.com",
    "google": "google.com",
    "github": "github.com",
    "gmail": "mail.google.com",
    "chatgpt": "chat.openai.com",
    "claude": "claude.ai",
    "reddit": "reddit.com",
    "twitter": "x.com",
    "x": "x.com",
    "instagram": "instagram.com",
    "linkedin": "linkedin.com",
    "netflix": "netflix.com",
    "amazon": "amazon.com",
    "wikipedia": "wikipedia.org",
    "stackoverflow": "stackoverflow.com",
    "leetcode": "leetcode.com",
    "whatsapp": "web.whatsapp.com",
    "spotify": "open.spotify.com",
    "drive": "drive.google.com",
    "maps": "maps.google.com",
    "translate": "translate.google.com",
    "colab": "colab.research.google.com",
}

def open_website(name):
    name = name.strip().lower()
    if name not in KNOWN_SITES and "." not in name:
        matches = get_close_matches(name, KNOWN_SITES.keys(), n=1, cutoff=0.6)
        if matches:
            print(f"(Interpreting '{name}' as '{matches[0]}')")
            name = matches[0]

    if name in KNOWN_SITES:
        url = KNOWN_SITES[name]
    else:
        url = name

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