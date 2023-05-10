import csv
import sqlite3

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

def 