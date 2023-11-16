from flask import Flask, render_template
import requests

app = Flask(__name__)

# JokeAPI endpoint for random jokes
JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

@app.route('/')
def index():
    # Fetch a random joke from the JokeAPI
    joke_data = fetch_joke()
    return render_template('index.html', joke_data=joke_data)

def fetch_joke():
    try:
        response = requests.get(JOKE_API_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        joke_data = response.json()
        return joke_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
