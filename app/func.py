import csv
import sqlite3
import random 
from db import * 

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

#input col(what column component) and input val(value of the column)
#return value of closest number
#pair with get_id(col, find_closest(col, val))
def find_closest(col, val):
    value = get_column(col)
    value = sorted(value)
    index = 0
    while (index < 170):
        maxx = value[index][0]
        if (maxx < val):
            index += 1
        else:
            prev = value[index-1][0]
            if (abs(val-prev) < abs(val-maxx)):
                return value[index-1][0]
            return value[index][0] 
    return value[index][0]

def buzzfeed():
    quizDict = {}
    quizDict[1] = [["danceability"], ["click me", "no", "no", "no"], [0.58, 0, 0, 0]]
    quizDict[2] = [["acousticness"], ["click me", "no", "no", "no"], [0.575, 0, 0, 0]]
    quizDict[3] = [["energy"], ["click me", "no", "no", "no"], [0.491, 0, 0, 0]]
    quizDict[4] = [["liveness"], ["click me", "no", "no", "no"], [0.121, 0, 0, 0]]
    # this song is supposed to be 'Tim McGraw'
    return quizDict

buzzfeed()



    
