from flask import Flask,render_template,request

from flask_mysqldb import MySQL

import mysql.connector

app = Flask(__name__)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="8885238264@kk",
    database="insta"
    )
mycursor=mydb.cursor()
mysql=MySQL(app)

    
@app.route('/', methods=['GET', 'POST'])

    
def index():


    if request.method == 'POST':
        username= request.form['username']
        passwords = request.form['password']


        #insert into db
        sql="INSERT INTO u_and_p (username,passwords) VALUES (%s,%s)"
        val=(username,passwords)
        mycursor.execute(sql,val)
        mydb.commit()
        cur = mysql.connection.cursor()

        return "Registration completed successfully"

    return render_template("index.html")
     
if __name__=="__main__":

    app.run(debug=True)
