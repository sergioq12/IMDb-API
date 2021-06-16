import requests
from movie import Movie

# Make the request

def requestAPI(queryStringInput):
    url = "https://imdb8.p.rapidapi.com/auto-complete"

    querystring = {"q":queryStringInput}

    headers = {
        'x-rapidapi-key': "aa3d1bb4bcmshd89c655c797d674p1232c0jsn10176ffb4551",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    # Doing the GET request to the API in order to get the response
    response = requests.request("GET", url, headers=headers, params=querystring)

    # making the response a json object (easier to work with)
    return response.json()

# with all the information gotten from the API, put that inside a list of movie objects that can be used to display
# the information in an HTML website
def getMovieInfo(movie_json):
    movies = []
    if "d" in movie_json:
        for movie in movie_json["d"]:
            # Only getting the movies that have all the requirements given by the WORD document
            if "y" in movie and "l" in movie and "i" in movie and "rank" in movie:
                if "imageUrl" in movie["i"]:
                    # After fulfilling the requirements, create a movie object, and append it to the list
                    print("Title: {title}. --> Released in: {year}. Ranked: #{rank}".format(title=movie["l"], year= movie["y"], rank=movie["rank"]))
                    movie_obj = Movie(title=movie["l"], year=movie["y"], rank=movie["rank"], imageUrl=movie["i"]["imageUrl"])
                    movies.append(movie_obj)

    return movies
        