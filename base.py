from flask import SQLAlchemy

db = SQLAlchemy()           #Using sql alchemy to save database

class Fcuser(db.Model): 
    __tablename__ = 'user'   #table name: user
    id = db.Column(db.Integer, primary_key = True)   #id as a primary key
    password = db.Column(db.String(64))     #Max length for the password = 64 
    userid = db.Column(db.String(32))       #Max length for the user id = 32
    username = db.Column(db.String(8))      #Max length for the username = 8