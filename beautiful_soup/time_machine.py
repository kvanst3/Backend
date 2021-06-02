from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
# from token import {"access_token"}



billboard_endpoint = "https://www.billboard.com/charts/hot-100/"
date = input("Which year you would like to travel to in YYYY-MM-DD:")

response = requests.get(billboard_endpoint + date)
page = response.text
soup = BeautifulSoup(page, "html.parser")

tags = soup.find_all(class_="chart-element__information__song text--truncate color--primary")
titles = [title.get_text() for title in tags]

tags = soup.find_all(class_="chart-element__information__artist text--truncate color--secondary")
artists = [artist.get_text() for artist in tags]


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

# sp = spotipy.Spotify(auth='BQDnEyxfNjIV89puZaxYwe5B-GNRvrdGKSyJvXYWo7eGfopoirQxmAHzSH81IQcnL3HZZDBeYyea056oDbJ3pZN0jzgWo7B_QQc0u-8iLBVzdqx7GP_U27zrTbkkLSwq08njj0hSSbH-bPTH07az--sFlWb30PobHgH7Gmdu3O46Sp5ph2Z9r1Lx54TzmnP_SQ')

song_uris = []
year = date.split("-")[0]
for song in titles:
    result = sp.search(q=f"artist:{artists[titles.index(song)]} track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)