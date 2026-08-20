import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Web Crawler Results\n")

for link in soup.find_all("a"):
    text = link.get_text(strip=True)
    href = link.get("href")

    if href:
        print("Text:", text)
        print("URL :", href)