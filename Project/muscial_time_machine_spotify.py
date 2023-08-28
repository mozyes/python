from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

question = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard_endpoint = "https://www.billboard.com/charts/hot-100/"
final_billboard_endpoint = billboard_endpoint + question

response = requests.get(final_billboard_endpoint)
response.raise_for_status()

content = response.text

soup = BeautifulSoup(content, 'html.parser')

all_songs = soup.select("li ul li h3")
all_songs_title = [song.getText(strip=True) for song in all_songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="Your own id here",
        client_secret="your own secret here",
        show_dialog=True,
        cache_path="token.txt",
        username="your user name here",
    )
)

song_uris = []
year = question.split("-")[0]
for song in all_songs_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped. ")

user_id = sp.current_user()["id"]

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{question} Billboard 100", public=False)
print(playlist)

# adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
