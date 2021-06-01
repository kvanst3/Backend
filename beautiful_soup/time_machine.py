from bs4 import BeautifulSoup
import requests


billboard_endpoint = "https://www.billboard.com/charts/hot-100/"
# date = input("Which year you would like to travel to in YYY-MM-DD:")
date = "1979-03-17"

response = requests.get(billboard_endpoint + date)
page = response.text
soup = BeautifulSoup(page, "html.parser")

tags = soup.find_all(class_="chart-element__information__song text--truncate color--primary")
titles = [title.get_text() for title in tags]
print(titles)