from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)

anchor_tag = soup.find_all("a")
# print(anchor_tag)

# for tag in anchor_tag:
#     print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))


