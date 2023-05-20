import sqlite3
import csv
DB_FILE = "file.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor() # Create the three tables if they dont exist yet
c.executescript("""
    create TABLE if NOT EXISTS user(u_id int primary key, username varchar(20), password varchar(30));
    create TABLE if NOT EXISTS songs(u_id int primary key, title text, album text, date text, length int, popularity float, danceability float, acousticness float, energy float, instrumentalness float, liveness float, loudness float, speechiness float, valence float, tempo float)
""")
c.close()

def get_username(id):
    c = db.cursor()
    c.execute("select username FROM user WHERE u_id = ?", (id,))
    result = c.fetchone()
    c.close()
    if(result == None):
        return None
    else:
        return result[0]

def get_password(id):
    c = db.cursor()
    c.execute("select password FROM user WHERE u_id = ?", (id, ))
    result = c.fetchone()
    c.close()
    if(result == None):
        return None
    else: 
        return result[0]

def register_new_user(username, password): # if username and password combination already exists, return False, else return ID
    c = db.cursor()
    c.execute("select exists(select 1 from user where username=? and password=?)", (username, password,)) # returns 1 if if already exists
    if (c.fetchone()[0] == 1):
        return -1
    c.execute("SELECT MAX(u_id) FROM user")
    max_id = c.fetchone()
    if (max_id[0] != None):
        new_id = max_id[0] + 1
    else:
        new_id = 0
    c.execute("insert into user values(? ,?, ?)", (new_id, username, password,))
    db.commit()
    c.close()
    return new_id

def account_match(username, password): # if it matches, return u_id, else return None
    c = db.cursor()
    c.execute('select u_id from user where (username = ? AND password = ?)', (str(username), str(password),))
    u_id = c.fetchone()
    c.close()
    if(u_id != None):
        return u_id[0]
    else:
        return None

def model_all_sql():
    c = db.cursor()
    id = 0
    with open('spotify_taylorswift.csv') as f:
        r = csv.DictReader(f)
        for row in r:
            c.execute("insert into songs values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, row["name"], row["album"], row["release_date"], row["length"], row["popularity"], row["danceability"], row["acousticness"], row["energy"], row["instrumentalness"], row["liveness"], row["loudness"], row["speechiness"], row["valence"], row["tempo"]))
            #c.execute("insert into songs values(?, ?)", (id, row["name"]))
            id = id+1

    db.commit()
    c.close()

def get_title(id):
    c = db.cursor()
    c.execute("select title FROM songs WHERE u_id = ?", (id, ))
    result = c.fetchone()
    c.close()
    if(result == None):
        return None
    return result[0]
def get_album(id):
    c = db.cursor()
    c.execute("select album FROM songs WHERE u_id = ?", (id, ))
    result = c.fetchone()
    c.close()
    if(result == None):
        return None
    return result[0]
def get_date(id):
    c = db.cursor()
    c.execute("select release_date FROM songs WHERE u_id = ?", (id, ))
    result = c.fetchone()
    c.close()
    if(result == None):
        return None
    return result[0]

#input column and value that matches 
#return u_id that matches 
def get_id(col, num):
    c = db.cursor()
    c.execute("select u_id FROM songs WHERE " + col + " = ?", (num, ))
    result = c.fetchone()
    c.close()
    if(result == None):
        return None
    return result[0]

#returns data for a certain song
#u_id[0], title[1], album[2], date[3], length[4], popularity[5], danceability[6], acousticness[7], energy[8], instrumentalness[9], liveness[10], loudness[11], speechiness[12], valence[13], tempo[14]
def get_data(id):
    c = db.cursor()
    c.execute("select * FROM songs WHERE u_id = ?", (id, ))
    result = c.fetchone()
    c.close()
    if(result == None):
        return None
    return result

#returns all data for a column of values
def get_col():
    c = db.cursor()
    result = []
    id = 0
    while (id <= 170):
        c.execute("select liveness FROM songs WHERE u_id = ?", (id, ))
        result.append(c.fetchone()[0])
        id = id+1
    c.close()
    if(result == None):
        return None
    return result 

# print(get_col())

# get all column data
def get_column(column_name):
    c = db.cursor()
    column_name = str(column_name)
    c.execute("select distinct(?) FROM songs", (column_name))
    result = c.fetchall()
    c.close()
    return result

# prints average value of selected albums
def get_average(column, album):
    c = db.cursor()
    c.execute("select avg(" + column + ") FROM songs GROUP BY album HAVING album = '" + album + "'")
    result = c.fetchall()
    c.close()
    return result

print(get_column("album"))