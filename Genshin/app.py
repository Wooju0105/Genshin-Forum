from flask import Flask, render_template, request, redirect
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

@app.route('/register', methods=['GET','POST']) #registering the user info.
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        #Create tne user info.
        userid = request.form.get('userid') 
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        print(password) #Check if there is actually a password.


        if not (userid and username and password and re_password) :
            return "Please fill out all of the form."
        elif password != re_password:
            return "Check the password again."
        else: #Successful output
            cursor = cursor()
            sql = "INSERT INTO user (userid, username, password, re_password) VALUES (?, ?, ?, ?)"
            cursor.execute(sql)
            results = cursor.fetchall()
            return "Successfully registered!", redirect('/home')

if __name__ == "__main__":
    app.run(debug=True)