from flask import Flask, render_template, request, redirect 
from base import db
import os
from base import Fcuser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contents")
def contents():
    return render_template("contents.html")

@app.route('/register', methods=['GET','POST'])
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
            return "Please fill all of the form."
        elif password != re_password:
            return "Check the password again."
        else: #모두 입력이 정상적으로 되었다면 밑에명령실행(DB에 입력됨)
            user = Fcuser()         
            user.password = password           #models의 FCuser 클래스를 이용해 db에 입력한다.
            user.userid = userid
            user.username = username      
            db.session.add(user)
            db.session.commit()
            return "Successfully registered!", redirect('/')

if __name__ == "__main__":
    app.run(debug=True)