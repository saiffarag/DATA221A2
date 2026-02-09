import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}

html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")

content_div = soup.find("div", id="mw-content-text")
if content_div is None:
    print("ERROR: Could not find div#mw-content-text")
    # optional: print a snippet to see what you got back
    print(soup.get_text()[:500])
    raise SystemExit

exclude_words = ["references", "external links", "see also", "notes"]
headings = []

for h2 in content_div.find_all("h2"):
    # Preferred: Wikipedia headline span
    span = h2.find("span", class_="mw-headline")
    if span:
        text = span.get_text(" ", strip=True)
    else:
        # Fallback: use h2 text
        text = h2.get_text(" ", strip=True)

    # Remove any [edit] text if it appears
    text = text.replace("[edit]", "").replace("edit", "").strip()

    # Skip empty headings
    if not text:
        continue

    # Exclude certain headings (case-insensitive contains)
    low = text.lower()
    if any(word in low for word in exclude_words):
        continue

    headings.append(text)

# Debug: show how many were found
print(f"Found {len(headings)} headings")

with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in headings:
        f.write(heading + "\n")
