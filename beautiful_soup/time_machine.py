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


user_sp_id = os.environ.get('SPOTIPY_CLIENT_ID')
user_sp_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=user_sp_id,
        client_secret=user_sp_secret,
        show_dialog=True,
        cache_path="beautiful_soup/token.txt"
    )
)
user_id = sp.current_user()["id"]