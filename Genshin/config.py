class Config(object):
    TITLE = 'Genshin Forum'
    DATABASE = 'sample.db'
    DEBUG = True
    SECRET_KEY = 'vision'


#@app.route('/register', methods=['GET','POST']) #registering the user info.
#def register():
 #   if request.method == 'GET':
  #      return render_template("register.html")
   ##    #Create tne user info.
       # userid = request.form.get('userid') 
     #   username = request.form.get('username')
      #  password = request.form.get('password')
        #re_password = request.form.get('re_password')
        #print(password) #Check if there is actually a password.


        #if not (userid and username and password and re_password) :
         #   return flash("Please fill out all of the form.")
        #elif password != re_password:
         #   return flash("Check the password again.")
        #else: #Successful output
         #   cursor = cursor()
          #  sql = "INSERT INTO user (userid, username, password, re_password) VALUES (?, ?, ?, ?)"
           # cursor.execute(sql)
            #results = cursor.fetchall()
            #return flash("Successfully registered!"), render_template("register.html", results=results), redirect("/home")