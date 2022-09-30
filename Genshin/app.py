from flask import Flask, render_template, request, redirect, session
from config import Config
import sqlite3

app = Flask(__name__)
app.config.from_object(Config) #brings "config" class from the config.py file. 

@app.context_processor
def header_title():
  return dict(title=app.config['TITLE']) #Displays the title on the config.py file as a header. 


@app.route("/")
def home():
    return render_template("home.html") #It directs to the homepage of the website

@app.route('/characters') #when the route is to /characters.
def characters():
    conn = sqlite3.connect(app.config['DATABASE']) #connects the database defined on the config.py.
    cur = conn.cursor()
    cur.execute("SELECT * FROM Characters ORDER BY id;") #There are multiple characters’ detailed information on the database and this sql query select all the info from the table on the database and order and display them by the id on the table.
    characters = cur.fetchall() #Fetches all the onfo on the table; CHaracters
    conn.close()
    return render_template("characters.html", characters=characters) #Directs the user to character.html webpage

@app.route('/characters/<int:id>') #Gets directed from the characters webpage and displays different information of the characters depends on the 'int'.
def des(id):
  conn = sqlite3.connect(app.config['DATABASE']) #connects the database defined on the config.py.
  cur = conn.cursor()
  cur.execute("SELECT * FROM Characters WHERE id=?;",(id,)) #Select a certain character from the list of four and directs to its own desciption webpage.
  characters = cur.fetchone()
  conn.close()
  return render_template("description.html", characters = characters) #Directs the user to description.html.

@app.route('/skills') #When the route is to /skills
def skills():
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM skills ORDER BY id;") # fetchone returns a certain data for one entry
    skills = cur.fetchall()
    conn.close()
    return render_template("skills.html", skills=skills)

@app.route('/skills/<int:id>') #Directs from skills webpage from tuple. 
def skill_des(id):
  conn = sqlite3.connect(app.config['DATABASE'])
  cur = conn.cursor()
  cur.execute("SELECT * FROM skills WHERE id=?;",(id,)) # fetchone returns a certain data for one entry
  skills = cur.fetchone()
  conn.close()
  return render_template("skills_des.html", skills = skills)

@app.route('/register', methods=['GET', 'POST']) #GET, POST methods to edit/add on the table of the database for the users details
def register():
        if request.method == 'GET':
            return render_template("register.html")

        if request.method == 'POST': #request userid, username, password, re_passowrd; these are the information that would go under each column of the table.
            userid = request.form['userid']
            username = request.form['username']
            password = request.form['password']
            re_password = request.form['re_password']
            conn = sqlite3.connect(app.config['DATABASE'])
            cs = conn.cursor()
            cs.execute('INSERT INTO user (userid, username, password, re_password) VALUES(?,?,?,?)',(userid,username,password,re_password)) #The input request by the users will be inserted into the table. 
            conn.commit() 
            conn.close()
        return redirect('/')

@app.route('/login_page', methods = ['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login_page.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        con = sqlite3.connect(app.config['DATABASE'])
        cursor = con.cursor()
        sql = "SELECT * FROM user WHERE username = ? AND password =?"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        print(result)
        if result:
            print("You are logged in")
            session["username"] = username
            return render_template('home.html')

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)