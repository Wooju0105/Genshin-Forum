from pydoc import render_doc
from flask import Flask, g, render_template,request,redirect, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

DATABASE = 'sample.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._databse = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/db")
def db():
    cursor = get_db().cursor()
    sql = "SELECT * FROM data"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contents")
def contents():
    return render_template("contents.html")


if __name__ == "__main__":
    app.run(debug=True)