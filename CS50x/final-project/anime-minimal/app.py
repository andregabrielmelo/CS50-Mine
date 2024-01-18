import os
import requests

from dotenv import load_dotenv, find_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import math

from functions_library import apology, login_required

# Get enviroment variables
load_dotenv() # Load variables from .env file
DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(12).hex())

# Database
con = sqlite3.connect(DATABASE_URL, check_same_thread=False) # Connect do database
db = con.cursor() # Create a cursor
# Create tables
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, hash BLOB NOT NULL)") # Users table
con.commit()
db.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)") # Notes table
con.commit()

# Configure application
app = Flask(__name__)

# Secret key
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    """Home Page"""

    # Get top airing animes 
    parameters = {
        "filter": "airing",
        "page": 1,
        "limit": 5,
    }
    request_TopAiringAnimes = requests.get("https://api.jikan.moe/v4/top/anime", params=parameters) # Request API 
    if request_TopAiringAnimes.status_code == 200: # If there was not a problem
        TopAiringAnimes = request_TopAiringAnimes.json()["data"] # Get anime data 
    else:
        return apology("Could not get top airing animes")

    # Get top upcoming animes
    parameters = {
        "filter": "upcoming",
        "page": 1,
        "limit": 5,
    }
    request_TopUpcomingAnimes = requests.get("https://api.jikan.moe/v4/top/anime", params=parameters) # Request API 
    if request_TopUpcomingAnimes.status_code == 200: # If there was not a problem
        TopUpcomingAnimes = request_TopUpcomingAnimes.json()["data"] # Get anime data 
    else:
        return apology("Could not get top upcoming animes")

    # TODO: Get most popular anime
    parameters = {
        "filter": "bypopularity",
        "page": 1,
        "limit": 5,
    }
    request_TopPopularAnimes = requests.get("https://api.jikan.moe/v4/top/anime", params=parameters) # Request API 
    if request_TopPopularAnimes.status_code == 200: # If there was not a problem
        TopPopularAnimes = request_TopPopularAnimes.json()["data"] # Get anime data 
    else:
        return apology("Could not get most popular animes")

    # Get top animes 
    parameters = {
        "page": 1,
        "limit": 5,
    }
    request_TopAnimes = requests.get("https://api.jikan.moe/v4/top/anime", params=parameters) # Request API 
    if request_TopAnimes.status_code == 200: # If there was not a problem
        TopAnimes = request_TopAnimes.json()["data"] # Get anime data 
    else:
        return apology("Could not get top animes")

    return render_template("index.html", TopAnimes=TopAnimes, TopPopularAnimes=TopPopularAnimes, TopAiringAnimes=TopAiringAnimes, TopUpcomingAnimes=TopUpcomingAnimes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register User"""

    # User reached out via POST 
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must have username")
        
        # Ensure password was submitted 
        if not request.form.get("password"):
            return apology("must have password")
        
        # Ensure confirmation was submitted 
        if not request.form.get("confirmation"):
            return apology("must confirm password")
        
        # Ensure the username is not taken
        existing_user = db.execute("SELECT username FROM users WHERE username = ?", (request.form.get("username"),)).fetchone()
        if existing_user is not None:
            return apology("Username already taken")

        # Ensure the password and confirmation are the same
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("The password and the confirmation must be the same")
        
        # Insert user into the database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (request.form.get("username"), generate_password_hash(request.form.get("password"))))
        con.commit()

        # Query database to get the id of the new user
        new_user = db.execute("SELECT id FROM users WHERE username = ?", request.form.get("username")).fetchone()
    
        # Remember wich user has registered
        session["user_id"] = new_user[0]

        # Redirect to the home page 
        return redirect("/")
    
    # User reached out via GET
    else:

        # Render page for the user to register
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log User In"""

    # Forget any user_id
    session.clear()

    # User reached out via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Must provide username")
        
        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("Must provide password")
        
        # Ensure username and password match
        userdata = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username")).fetchall()
        if len(userdata) == 0: # Check if the user exists
            return apology("User does not exist")
        if not check_password_hash(userdata[0][2], request.form.get("password")):
            return apology("Username or password invalid")
        
        # Remember which user has logged in 
        session["user_id"] = userdata[0][0]

        # Redirect user to home page    
        return redirect("/")
    
    # User reached out via get
    else:

        # Render page to log in
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log User Out"""

    # Forget any user id 
    session.clear()

    # Redirect user to home page
    return redirect("/")


@app.route("/search", methods=["GET", "POST"])
def search():
    """Show search form"""

    # User reached out via POST
    if request.method == "POST":

        # See if the was not an input form the user
        all_none = all(value is '' for value in list(request.form.values()))

        # If there was no input
        if all_none:
            flash("Input is needed for search")
            return redirect("/search")

        # Get name 
        if request.form.get("name"):
            requested_name = request.form.get("name")
        else:
            requested_name = None

        # Get type
        if request.form.get("type"):
            requested_type = request.form.get("type").lower()
        else:
            requested_type = None

        # Get score 
        if request.form.get("score"):
            min_score = int(request.form.get("score"))
        else:
            min_score = None

        # Get status
        status = ["Currently Airing", "Finished Airing", "Not Yet Aired"]
        true_status = ["airing", "complete", "upcoming"]

        selected_status = request.form.get("status")

        if selected_status in status:
            index = status.index(selected_status)
            requested_status = true_status[index]
        else:
            requested_status = None

        # Get producer id
        p = {
            "q": request.form.get("producer"),
        }

        if request.form.get("producer"):
            requested_producer = requests.get("https://api.jikan.moe/v4/producers", params=p)
            requested_producer = requested_producer.json()["data"][0]["mal_id"] 
        else:
            requested_producer = None

        # Get rating 
        ratings = ["G: All Ages", "PG: Children", "PG-13: Teens 13 or Older", "R: 17+ (Violence & Profanity)", "R+: Mild Nudity", "RX: Hentai"]
        # Initialize a variable to store the requested ratings
        requested_ratings = None
        # Get the selected rating from the form
        selected_rating = request.form.get("ratings")
        # Find the matching rating in the list
        for row in ratings:
            if row == selected_rating:
                # Split the string by colon and get the part before the colon
                requested_ratings = row.split(":")[0].strip()

        else:
            requested_ratings = None

        # Get genres
        requested_genres = [] 
        if request.form.getlist("genre"):
            genres = request.form.getlist("genre")
            request_anime_genres = requests.get("https://api.jikan.moe/v4/genres/anime")
            for i in range(len(request_anime_genres.json()["data"])):
                for j in range(len(genres)):
                    if genres[j] in request_anime_genres.json()["data"][i]["name"]:
                        requested_genres.append(request_anime_genres.json()["data"][i]["mal_id"])
        else:
            requested_genres = None

        # Get order
        if request.form.get("order_by"):
            requested_order = request.form.get("order_by")
        else:
            # Ordered by rank by default
            requested_order = "rank"

        # Get sort
        if request.form.get("order_type"):
            requested_orderType = request.form.get("order_type")
        else:
            # Order ascending by default
            requested_orderType = "asc"

        # Parameters
        parameters = {
            "q": requested_name,
            "limit": 25,
            "type": requested_type,  # Replace with the actual value
            "min_score": min_score,  # Replace with the actual value
            "status": requested_status,
            "producers": requested_producer,
            "rating": requested_ratings,
            "genres" : requested_genres,
            "order_by": requested_order,
            "sort": requested_orderType,
        }

        # Redirect to animes page with parameters
        return redirect(url_for('animes', page=1, **parameters))

    # User reached out via GET
    else:

        # Types (sorted alphabetically)
        types = ["CM", "Movie", "Music", "ONA", "OVA", "PV", "Special", "TV", "TV Special"]
        types.sort()

        # Status (sorted alphabetically)
        status = ["Currently Airing", "Finished Airing", "Not Yet Aired"]
        status.sort()

        # Get producers (sorted alphabetically)
        producers = []
        request_producers = requests.get("https://api.jikan.moe/v4/producers")
        if request_producers.status_code == 200:
            for i in range(len(request_producers.json()["data"])):
                producers.append(request_producers.json()["data"][i]["titles"][0]["title"])

        # Rated (sorted alphabetically)
        ratings = ["G: All Ages","PG: Children","PG-13: Teens 13 or Older", "R: 17+ (Violence & Profanity)", "R+: Mild Nudity", "RX: Hentai"]
        ratings.sort()

        # Get anime genres
        genres = []
        request_animeGenres = requests.get("https://api.jikan.moe/v4/genres/anime")
        if request_animeGenres.status_code == 200:
            for i in range(len(request_animeGenres.json()["data"])):
                genres.append(request_animeGenres.json()["data"][i]["name"])

        # Orders (sorted alphabetically)
        orders_by = ["title", "episodes", "score", "rank"]
        orders_by.sort()

        # Ascending or descending
        order_type = {"asc":"Ascending", "desc":"Descending"}

        # Render search page
        return render_template("search.html", types=types, status=status, producers=producers, ratings=ratings, genres=genres, orders_by=orders_by, order_type=order_type, show=False)


@app.route("/animes/<int:page>")
def animes(page):
    """Show a list of animes to user"""

    # Get parameters
    parameters_without_page = request.args.to_dict()
    parameters = request.args.to_dict()
    parameters['page'] = page # add page to parameters
    
    # Get animes
    request_animes = requests.get("https://api.jikan.moe/v4/anime", params=parameters)

    # Get anime data and pagination
    anime_data = request_animes.json()["data"]
    page = request_animes.json()["pagination"]

    # Filter anime data excluding those without rank
    anime_data = [anime for anime in anime_data if anime.get('rank') is not None]

    # Sort anime data based in rank
    anime_data = sorted(anime_data, key=lambda x: x['rank'])

    # Total pages 
    total_results = page["items"]["total"]
    results_per_page = page["items"]["per_page"]
    total_pages = total_results/results_per_page
    total_pages = math.ceil(total_pages)

    # Create a dictionary representing the pagination information
    page_obj = {
        'number': page["current_page"],
        'has_previous': page["current_page"] > 1,
        'has_next': page["current_page"] < total_pages,
        'previous_page_number': page["current_page"] - 1,
        'next_page_number': page["current_page"] + 1,
        'total_pages': total_pages,
    }

    # Render page with animes
    return render_template("animes.html", anime_data=anime_data, page_obj=page_obj, parameters_without_page=parameters_without_page)

@app.route("/anime/<int:id>") 
def anime(id):
    """Show Anime Page"""

    # Get anime by id
    request_anime = requests.get(f"https://api.jikan.moe/v4/anime/{id}/full")
    print(request_anime.url)

    # Check if the request was successful
    if request_anime.status_code == 200:
        # Extract data 
        anime = request_anime.json()["data"]
    else:
        return apology("Invalid anime ID", code=404)

    # User reached out via GET 
    return render_template("anime.html", anime=anime)  
    

@app.route("/ranking/<int:page>")
def ranking(page=1):

    # Add page to parameters 
    parameters = {
        "page": page,
    }

    # Get top animes 
    request_TopAnimes = requests.get("https://api.jikan.moe/v4/top/anime", params=parameters)

    # Check if the request was successful
    if request_TopAnimes.status_code == 200:
        # Extract data for the top animes
        anime_data = request_TopAnimes.json()["data"]

    # Filter out items with None rank
    filtered_anime_data = [anime for anime in anime_data if anime.get('rank') is not None]

    # Sort the filtered anime data by rank
    anime_data = sorted(filtered_anime_data, key=lambda x: x['rank'])

    # Get pagination 
    page_obj = request_TopAnimes.json()["pagination"]

    # Render page with animes
    return render_template("ranking.html", anime_data=anime_data, page_obj=page_obj)


@app.route("/notes", methods=["GET", "POST"])
@login_required
def notes():

    # User reached out via POST
    if request.method == "POST":

        # If deleted
        if 'delete' in request.form:
            existing_notes = db.execute("SELECT content FROM notes WHERE id = ?", (session["user_id"],)).fetchone()
            if existing_notes:
                db.execute("UPDATE notes SET content = ? WHERE id = ?", (None, session["user_id"]))

        # Get what was typed 
        if request.form.get("typed"):
            
            # Check if the user already has notes
            existing_notes = db.execute("SELECT content FROM notes WHERE id = ?", (session["user_id"],)).fetchone()
            
            if existing_notes:
                # User has existing notes, update them
                if existing_notes[0] != None:
                    updated_notes = existing_notes[0] + request.form.get("typed") + '/0'
                else: 
                    updated_notes = request.form.get("typed") + '/0'
                db.execute("UPDATE notes SET content = ? WHERE id = ?", (updated_notes, session["user_id"]))
            else:
                # User doesn't have existing notes, insert a new row
                db.execute("INSERT INTO notes (content, id) VALUES (?, ?)", (request.form.get("typed"), session["user_id"]))

            con.commit()

        # Restart page with GET request 
        return redirect("/notes")

    # User reached out via GET 
    else:
        # Get user notes
        user_notes = db.execute("SELECT content FROM notes WHERE id = ?", (session["user_id"], )).fetchall()

        # Render notes page 
        return render_template("notes.html", user_notes=user_notes)

