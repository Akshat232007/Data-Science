from bs4 import BeautifulSoup

with open("Demo.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

title = soup.title.string
heading = soup.h1.string
paragraph = soup.p.string

print("Title:", title)
print("Heading:", heading)
print("Paragraph:", paragraph)
