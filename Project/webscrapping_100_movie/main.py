from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

content = response.text

soup = BeautifulSoup(content, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
