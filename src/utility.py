import requests
import json
config = json.load(open("config.json"))

OMDB_API_KEY = config["OMDB_API_KEY"]

def get_movie_details(title, OMDB_API_KEY):

    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={OMDB_API_KEY}"
    res = requests.get(url).json()
    if res.get("Response") == "True":
        result = res.get("Plot", "N/A"), res.get("Poster", "N/A")
        plot = result[0]
        poster = result[1]
        return plot, poster

    return "N/A", "N/A"
