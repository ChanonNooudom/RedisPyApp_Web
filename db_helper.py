import sqlite3
import time


from redis import Redis
con = sqlite3.connect("tutorial.db")


def CreateTable(query):
    cur = con.cursor()
    cur.execute(query)

def Select(query):
    cur = con.cursor()
    res = cur.execute(query)
    return res.fetchall()

def Insert(query, *data):
    cur = con.cursor()
    cur.execute(query.format(data))
    con.commit()

def Delete(query):
    cur = con.cursor()
    cur.execute(query)
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