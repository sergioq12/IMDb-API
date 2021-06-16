from flask.helpers import url_for
from initApp import app
from flask import render_template, request, session, redirect, url_for
from flask_session import Session
from movieRequest import *

Session(app)

@app.route("/")
def index():
    if session.get("history") is None:
        session["history"] = []
    return render_template("index.html")

@app.route("/movies", methods=["GET", "POST"])
def movies():
    movie_request = request.form.get("search-request")
    if len(session['history']) == 10:
        del session['history'][len(session['history'])-1]
    session["history"].insert(0,movie_request)

    # making the api call and getting the information back as a json object
    movie_response_json = requestAPI(movie_request)

    # getting the json object organized as a list with movie objects
    movieObjs = getMovieInfo(movie_response_json)
    if len(movieObjs) == 0:
        movieObjs = False

    return render_template("movie-results.html", movies= movieObjs, movie_request=movie_request)

@app.route("/movies/history", methods=["GET"])
def history():
    refreshing = True
    if len(session['history']) == 0:
        refreshing = False
    return render_template("history.html", history = session['history'], refreshing=refreshing)

@app.route("/movies/history/refresh")
def refresh():
    session['history'] = []
    return redirect(url_for('history'))

@app.route("/movies/information")
def information():
    return render_template("information.html")
    
    



if __name__ == "__app__":
    app.run(debug=True)