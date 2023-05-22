from flask import Flask, session, render_template, request, redirect, url_for
from db import *
from func import *  
import sqlite3
import csv

app = Flask(__name__)
app.secret_key = "temp"

@app.route("/login", methods=["GET", "POST"])
def login():
    if ( request.method == "GET" ):
        return render_template("login.html") # This is for accessing the page
    Input0 = request.form.get("username")
    Input1 = request.form.get("password")
    session_id = account_match(Input0, Input1)
    if ( session_id != None ):
        session["ID"] = session_id
        return redirect(url_for("home_page"))
    return render_template("login.html", status="Username and passwords do not match.")

@app.route("/", methods=["GET", "POST"])
def home_page():
    dataDict = model_all()
    if(session.get("ID", None) == None):
        return redirect(url_for("login"))
    elif (get_username(session.get("ID")) == None):
        return redirect(url_for("login"))
    else:
        session_user = F"{get_username(session['ID'])}"
        model_all()
        #print(session_user)
    return render_template("home_page.html", data=dataDict, user=session_user) #status=stat

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("ID",None) # removes session info, retunrs nothing if not there
    return redirect(url_for("login", status="Please login"))

@app.route("/register", methods=["GET", "POST"])
def register_page():
    if( request.method == "GET"): # display page
        return render_template("register.html")
    Input0 = request.form.get("username")
    Input1 = request.form.get("password")
    Input2 = request.form.get("confirmation")
    # issue of session_id referenced before assignment in line 50
    # Session_id = register_new_user(Input0, Input1)
    if Input1 == Input2:
        Session_id = register_new_user(Input0, Input1)
        if( Session_id != -1 ): # see if new user info is already in use, if not then sign them in
            session["ID"] = Session_id
            return redirect(url_for("home_page"))
        return render_template("register.html", status="Login info is in use.")
    else:
        return render_template("register.html", status="Passwords do not match.")

@app.route("/analysis", methods=["GET", "POST"])
def analysis_page():
    if(session.get("ID", None) == None):
        return redirect(url_for("login"))
    session_user = F"{get_username(session['ID'])}"

    data = get_column("album")
    album = get_column("album")
    column = ["length", "popularity", "danceability", "acousticness", 
            "energy", "instrumentalness", "liveness", "loudness", 
            "speechiness", "valence","tempo"]

    data = []
    data +=album
    for i in album:
        for j in column:
            datum = get_average(j, str(i)[2: len(str(i))-3])
            data+=datum

    return render_template("analysis.html", user=session_user, data=data)

@app.route("/buzzfeed", methods=["GET", "POST"])
def buzzfeed_page():
    buzz = buzzfeed()
    if(session.get("ID", None) == None):
        return redirect(url_for("login"))
    session_user = F"{get_username(session['ID'])}"

    if(request.method == "POST"):
        #add up values for all selections
        result = [0, 0, 0, 0]
        for question in buzz:
            #vals is returned as a string, so get in list format
            vals = request.form.get(question)
            if (vals == None):
                return redirect(url_for("buzzfeed_page"))
            vals = vals[1:len(vals)-1]
            vals = vals.split(", ")
            index = 0
            while (index < 4):
                result[index] = float(result[index]) + float(vals[index])
                index += 1
        #get average 
        index = 0
        while (index < 4):
            result[index] = result[index]/4
            index += 1
        song = find_closest_2(result)
        add_buzzfeed(session_user, song, result)
        return render_template("buzzfeed.html", data=buzz, user=session_user, answer=True, result=song)

    return render_template("buzzfeed.html", data=buzz, user=session_user, answer=False)

@app.route("/find_song", methods=["GET", "POST"])
def favorite_songs_page():
    if(session.get("ID", None) == None):
        return redirect(url_for("login"))
    session_user = F"{get_username(session['ID'])}"

    if(request.method=="POST"):
        dance = float(request.form.get("dance_range"))/100
        acoust = float(request.form.get("acoust_range"))/100
        energy = float(request.form.get("energy_range"))/100
        live = float(request.form.get("live_range"))/100
        song = find_closest_2([dance, acoust, energy, live])
    else:
        song = ""

    return render_template("find_song.html", similar_song=song, user=session_user)

@app.route("/profile", methods=["GET", "POST"])
def profile_page():
    if(session.get("ID", None) == None):
        return redirect(url_for("login"))
    session_user = F"{get_username(session['ID'])}"
    buzzData = get_buzzfeed(session_user)
    return render_template("profile.html", buzzfeedData=buzzData, user=session_user)

@app.route("/user_stats", methods=["GET", "POST"])
def user_stats_page():
    if(session.get("ID", None) == None):
        return redirect(url_for("login"))
    session_user = F"{get_username(session['ID'])}"

    return render_template("user_stats.html", user=session_user)

if __name__ == "__main__":
    app.debug = True
    app.run()