from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.a)
