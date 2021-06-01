from bs4 import BeautifulSoup

# with open('beautiful_soup/website.html') as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# url = soup.select_one(selector="p a")
# print(url)

# name = soup.select_one("#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

import requests

response = requests.get('https://news.ycombinator.com/')
page = response.text
soup = BeautifulSoup(page, "html.parser")

all_scores = s = soup.find_all(name='span', class_="score")
highest_score = 0
high_score_index = 0
for score in all_scores:
    num_score = int(score.get_text().split()[0])
    if num_score > highest_score:
        highest_score = num_score
        high_score_index =  all_scores.index(score)

highest_post_id = all_scores[high_score_index].get("id").split("_")[1]
element = soup.find(attrs={"id": highest_post_id})
target = element.find(class_="storylink")
print(target.get_text())
print(target.get("href"))