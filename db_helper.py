import sqlite3
import time

from redis import Redis
con = sqlite3.connect("tutorial.db")


def CreateDb():
    cur = con.cursor()
    cur.execute("CREATE TABLE movie(title, year, score, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")

def ReadDb():
    cur = con.cursor()
    res = cur.execute("SELECT * FROM movie")
    return res.fetchall()

def InsertDb(val1, val2, val3):
    cur = con.cursor()
    cur.execute("INSERT INTO movie (title, year, score) VALUES ( '{}', '{}', '{}' )".format(val1, val2, val3))
    con.commit()

def DeleteDb(key_value):
    cur = con.cursor()
    cur.execute("DELETE FROM movie ")
    con.commit()

def DeleteTable():
    cur = con.cursor()
    cur.execute("DROP TABLE movie")
    con.commit

def GenerateTable(data):
    result = ""
    result += "<table>"
    result += "<tbody>"
    for d in data:
        result += "<tr>"
        for col in range(len(d)):
            result += "<td>{}</td>".format(d[col])
        result += "</tr>"
    result += "</tbody>"
    result += "<table>"
    return result
            
   
 
# DeleteTable()
#CreateDb()
# DeleteDb('G')
# for i in range(10):
#     InsertDb(str(i), str(i + 2000), str(21))
#     time.sleep(2)

# InsertDb('G', '2011', '3')


# a = ReadDb()
# print(len(a))
# for b in a:
#     print(b)