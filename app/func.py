import csv
import sqlite3
import random 
from db import * 

dance_list = get_column("danceability")
acoust_list = get_column("acousticness")
energy_list = get_column("energy")
live_list = get_column("liveness")

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

def model_all_specified(arr):
    dataDict = {}
    with open('spotify_taylorswift.csv') as f:
        r = csv.DictReader(f)
        for row in r:
            song_elements = []
            albumName = row["album"]
            if (albumName not in dataDict):
                dataDict[albumName] = []
            song_elements.append(row["name"])
            for element in arr:
                song_elements.append(row[element])
            dataDict[albumName].append(song_elements)
    return dataDict

def rand_func():
    rand = random.randint(0,170)
    return rand

#input col(what column component) and input val(value of the column)
#return u_id of song with closest value
#pair with get_id(col, find_closest(col, val))
def find_closest_one(col, val):
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
                return get_id(col, prev)
            return get_id(col, maxx) 
    return value[index][0]

#print(find_closest_one("danceability", 0.41))

#each song has total point value, all start at 0 
#go down each col value and check the value of the song compared to the chosen value 
#if chosen value and value of the song are identical 100 points are rewarded 
#the closer the value is to the chosen value, the more points awarded
#the further the value is to the chosen value, the less points awarded 
#each category should be scaled to 100 
#all points are added up at the end, and the song(s) with highest points are returned  
#INPUT: array of val for cols in this order [danceability, acouticness, energy, liveness]
def find_closest(arr):
    result = []
    index = 0
    while (index <= 170):
        result[index] = 0
        index += 1
    cols = ["danceability", "acouticness", "energy", "liveness"]
    #for col in cols: 
        #loop through each song
    return result

#INPUT: [danceability, acouticness, energy, liveness]
def find_closest_2(arr):
    #initializing array to set point values for a song
    points = []
    dataDict = model_all_specified(["danceability", "acousticness", "energy", "liveness"])
    for album in dataDict:
        for song in dataDict[album]:
            songName = song[0]
            songPoints = 0
            for num in range(len(arr)):
                songPoints += abs(1.0-(float(song[num+1])/arr[num]))
            points.append([songName, songPoints])
    topSong = ""
    topPoints = 100
    for song in points:
        if (song[1]<topPoints):
            topPoints = song[1]
            topSong = song[0]
    return topSong

#print(find_closest_2([0.58, 0.575, 0.491, 0.121]))
#print(find_closest_2([0.57, 0.57, 0.49, 0.1]))
#print(find_closest_2([0.3, 0.34, 0.67, 0.1]))

#def buzzfeed():
#    quizDict = {}
#    quizDict[1] = [["danceability"], ["click me", "no", "no", "no"], [0.58, 0, 0, 0]]
#    quizDict[2] = [["acousticness"], ["click me", "no", "no", "no"], [0.575, 0, 0, 0]]
#    quizDict[3] = [["energy"], ["click me", "no", "no", "no"], [0.491, 0, 0, 0]]
#    quizDict[4] = [["liveness"], ["click me", "no", "no", "no"], [0.121, 0, 0, 0]]
#    # this song is supposed to be 'Tim McGraw'
#    return quizDict

#answer choice + values it contributes for each category  ["danceability", "acousticness", "energy", "liveness"]

def buzzfeed():
    #questions = ["q1", "q2", "q3", "q4"]
    quizDict = {
        "Favorite Scent?": [["Spilled fabric softener", [0.58, 0.575, 0.491, 0.121]], ["Charred barbeque roast", [0.708, 0.101, 0.601, 0.0979]], ["Tires streaking on wet pavement", [0.602, 0.0773, 0.896, 0.0911]], ["Eggs cooked in sesame oil", [0.613, 0.0527, 0.764, 0.197]]],
        "Go-To Phrase?": [["Bonkers...", [0.576, 0.051, 0.777, 0.32]], ["Bazinga!", [0.57, 0.445, 0.747, 0.219]], ["Preposterous :(", [0.505, 0.035, 0.443, 0.0906]], ["Weewooweewoo", [0.661, 0.921, 0.151, 0.13]]],
        "Best Programming Language?": [["SQL", [0.418, 0.217, 0.482, 0.123]], ["Python", [0.715, 0.829, 0.308, 0.16]], ["Java", [0.53, 0.199, 0.526, 0.14]], ["C", [0.433, 0.907, 0.182, 0.123]]],
        "Favorite CS Teacher?": [["Homes", [0.479, 0.525, 0.578, 0.0841]], ["Topher!!!", [0.61, 0.505, 0.556, 0.0851]], ["DEEEEEEE-W", [0.605, 0.00201, 0.725, 0.101]], ["K.O", [0.316, 0.878, 0.361, 0.0797]]]
    }
    return quizDict

#buzzfeed()
