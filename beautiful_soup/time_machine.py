from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os



# billboard_endpoint = "https://www.billboard.com/charts/hot-100/"
# date = input("Which year you would like to travel to in YYYY-MM-DD:")

# response = requests.get(billboard_endpoint + date)
# page = response.text
# soup = BeautifulSoup(page, "html.parser")

# tags = soup.find_all(class_="chart-element__information__song text--truncate color--primary")
# titles = [title.get_text() for title in tags]


user_id = os.environ.get('SPOTIPY_CLIENT_ID')
spotify_endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"


headers = {
    
}

response = requests.get(url=endpoint, headers=headers)
# response.raise_for_status()
print(response.text)