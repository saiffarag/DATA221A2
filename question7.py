import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")

# Safely extract title
title_tag = soup.find("title")
if title_tag:
    print(title_tag.get_text(strip=True))
else:
    print("Title not found")

# Extract first paragraph with at least 50 characters
content_div = soup.find("div", id="mw-content-text")

if content_div:
    for p in content_div.find_all("p"):
        text = p.get_text(" ", strip=True)
        if len(text) >= 50:
            print(text)
            break
