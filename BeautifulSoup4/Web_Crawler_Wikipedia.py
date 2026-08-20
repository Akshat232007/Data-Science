import requests
from bs4 import BeautifulSoup
url = "https://www.wikipedia.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print("First 3 Paragraphs:")
paragraphs = soup.find_all("p")
for p in paragraphs[:3]:
    print(p.get_text(strip=True))
    print()
print("Image URLs:")

images = soup.find_all("img")
for img in images:
    print(img.get("src"))
    
links = soup.find_all("a")

print("\nTotal Number of Links:", len(links))

print("\nHeadings:")
headings = soup.find_all(["h1", "h2", "h3"])
for heading in headings:
    print(heading.get_text(strip=True))

print("\nLanguages:")
languages = soup.find_all("div", class_="central-featured-lang")
for language in languages:
    name = language.find("strong")
    
    if name:
        print(name.get_text(strip=True))