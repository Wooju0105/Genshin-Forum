from flask import Flask, flash, render_template, request, redirect, session
from config import Config
import sqlite3
import random

app = Flask(__name__)
app.config.from_object(Config)

@app.context_processor
def pre_made():
  return dict(title=app.config['TITLE'])


@app.route("/")
def home():
    return render_template("home.html") #homepage of the website

@app.route('/characters')
def characters():
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM Characters ORDER BY id;")
    characters = cur.fetchall()
    conn.close()
    return render_template("characters.html", characters=characters)

@app.route('/characters/<int:id>')
def des(id):
  conn = sqlite3.connect(app.config['DATABASE'])
  cur = conn.cursor()
  cur.execute("SELECT * FROM Characters WHERE id=?;",(id,))
  characters = cur.fetchone()
  conn.close()
  return render_template("description.html", characters = characters)

@app.route('/comment', methods=["GET","POST"])
def comment():
    if request.method == "POST":
        conn = sqlite3.connect(app.config['DATABASE'])
        cur = conn.cursor()
        title = request.form["title"]
        feedback = request.form["feedback"]
        sql = "INSERT INTO "

@app.route('/register', methods=['GET', 'POST'])
def register():
        if request.method == 'GET':
            return render_template("register.html")

        if request.method == 'POST':
            userid = request.form['userid']
            username = request.form['username']
            password = request.form['password']
            re_password = request.form['re_password']
            conn = sqlite3.connect(app.config['DATABASE'])
            cs = conn.cursor()
            cs.execute('INSERT INTO user (userid, username, password, re_password) VALUES(?,?,?,?)',(userid,username,password,re_password))
            conn.commit()
            conn.close()
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)