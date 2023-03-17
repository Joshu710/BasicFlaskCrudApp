from flask import *
import sqlite3
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')


def getplayers():
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'players'")
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/add",methods=["POST","GET"])
def addtodb():
    print("hi")
    msg = ""
    if request.method == "POST":
        try:
            name = request.form["name"]  
            mid = request.form["mid"]  
            pscore = request.form["pscore"] 
            with sqlite3.connect("players.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into players (name, id, score) values (?,?,?)",(name,mid,pscore))  
                con.commit()
                msg = name + " was added"
        except:
            con.rollback()
            msg = name + " was not added"
        con.close()
    return render_template("index.html", mesg=msg)
    


@app.route("/delete",methods=["POST","GET"])
def delplayer():
    msg = ""
    if request.method == "POST":
        try:
            name = request.form["searching"]
            print(name)
            with sqlite3.connect("players.db") as con: 
                cur = con.cursor()
                cur.execute("DELETE FROM players WHERE name='" + name +"'")
                con.commit()
                msg = name + " was deleted"
        except:
            con.rollback()
            msg = name + " was not deleted"
        con.close()
    return render_template("delete.html",mesg=msg)


@app.route("/search",methods=["POST","GET"])
def searchplayer():
    msg = ""
    res = []
    if request.method == "POST":
        try:
            name = request.form["searching"]
            print(name)
            with sqlite3.connect("players.db") as con: 
                cur = con.cursor()
                res = cur.execute("SELECT * FROM 'players' WHERE name LIKE'%" + name +"%';")
                res = res.fetchall()
        except:
            msg = name + " was not found"
        con.close()
    return render_template("search.html",mesg=msg,res=res)



if __name__ == "__main__":
    app.run()