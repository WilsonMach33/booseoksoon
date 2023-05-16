import csv
import sqlite3
import random 
# modeling .csv data
def model_all():
    dataDict = {}
    #dataDict["name"] = []
    #dataDict["album"] = []
    with open('spotify_taylorswift.csv') as f:
        r = csv.DictReader(f)
        for row in r:
            albumName = row["album"]
            if (albumName not in dataDict):
                dataDict[albumName] = []
            dataDict[albumName].append(row["name"])
    return dataDict

def rand_func():
    rand = random.randint(0,170)
    return rand

def match_song(input):
    liveness = get_col()

def buzzfeed():
    quizDict = {}
    quizDict[1] = [["danceability"], ["click me", "no", "no", "no"], [0.58, 0, 0, 0]]
    quizDict[2] = [["acousticness"], ["click me", "no", "no", "no"], [0.575, 0, 0, 0]]
    quizDict[3] = [["energy"], ["click me", "no", "no", "no"], [0.491, 0, 0, 0]]
    quizDict[4] = [["liveness"], ["click me", "no", "no", "no"], [0.121, 0, 0, 0]]
    # this song is supposed to be 'Tim McGraw'

    