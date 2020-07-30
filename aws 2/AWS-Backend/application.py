import mysql.connector
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS



conn=mysql.connector.connect(host="database-2.cjotctvimnwg.us-east-2.rds.amazonaws.com",user="admin",password="admin302",database="bikedb")


mycursor=conn.cursor()

application = Flask(__name__)
CORS(application)

@application.route('/')
def index():
    mycursor.execute("SELECT * FROM Bike ")
    data=mycursor.fetchall()
    return render_template('index.html',data=data)
@application.route('/add')
def add():
    return render_template('addbikes.html')

@application.route('/insert', methods=['POST'])
def insert():
    name = request.form.get('name')
    cost = request.form.get('cost')
    varient = request.form.get('varient')
    poster = request.form.get('poster')

    mycursor.execute("INSERT INTO Bike (id,name,cost,varient,poster) VALUES (NULL,'{}','{}','{}','{}')".format(name,cost,varient,poster))
    conn.commit()

    return render_template('addbikes.html')

@application.route('/view/<bikes>',methods=['GET'])
def view_Bike(bikes):

    mycursor.execute("SELECT * FROM Bike WHERE name LIKE '{}'".format(bikes))
    data = mycursor.fetchall()
    if(len(data)!=0):
        response={'response':200, 'data':{'name':data[0][1], 'cost':data[0][2], 'varient':data[0][3], 'poster':data[0][4]}}
    else:
        response={'response':404}
    return jsonify(response)





if __name__=="__main__":
    application.run(debug=True)





#On DB Server we will create our database

#mycursor.execute("CREATE DATABASE bikedb")


#Creating table

#mycursor.execute("CREATE TABLE Bike (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(30) NOT NULL,Cost VARCHAR(30) NOT NULL,Varient VARCHAR(50) NOT NULL, poster VARCHAR(255))")


#INSERT Data


#mycursor.execute("INSERT INTO Bike(Id,Name,Cost,Varient,poster) VALUES(NULL,'DUKE 200','2.05 L','2020','https://www.ktm.com/ktmgroup-storage/PHO_BIKE_90_RE_200DUKE-MY20-Orange-PHO-BIKE-90-RE_%23SALL_%23AEPI_%23V1.png')")
#conn.commit()

#mycursor.execute("SELECT * FROM Bike")
#data=mycursor.fetchall()
#print(data)
