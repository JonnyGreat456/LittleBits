# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, render_template,request
from flask_socketio import SocketIO,emit
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

login_user_busser = ""

@app.route("/busserlogin/")
def busserlogin():
	return render_template("busserlogin.html")

@app.route('/loginverifybusser',methods = ['POST', 'GET'])
def loginverifybusser():
	if request.method == 'POST':
		uname = request.form['uname']
		pword = request.form['psw']
		conn = sqlite3.connect('busserprofile.db')
		cursor = conn.execute("SELECT Name,Username,Password,Row FROM Bussers")
		for row in cursor:
			print row[1]
			print row[2]
			if(uname == row[1] and pword == row[2]):
				global login_user_busser
				login_user_busser=row[0]
				return render_template("bussermainpage.html",name=row[0])
	if request.method =='GET':
		print(login_user_busser)
		return render_template("bussermainpage.html",name=login_user_busser)
	return render_template('busserlogin.html')

@app.route('/signupbusser',methods = ['POST','GET'])
def signupbusser():
	pay=0
	if request.method == 'POST':
		fullname = request.form['name']
		position = request.form['role']
		dob = request.form['dob']
		phone_number = request.form['phone']
		pword = request.form['pword']
		uname = request.form['uname']
		if position=="chef":
			pay=25
		if position=="waiter":
			pay=18
		if position=="busser":
			pay=9
		
		conn = sqlite3.connect('busserprofile.db')
		cursor = conn.execute("SELECT Name,POSITION,DOB,Phone,Pay,Username,Password from Bussers")
		for row in cursor:
			conn.execute("INSERT INTO Bussers (Row,Name,POSITION,DOB,Phone,Pay,Username,Password) \
				VALUES (NULL,?,?,?,?,?,?,?)",(fullname, position, dob,phone_number,pay,uname,pword));
			conn.commit()
			print "Records created successfully"
			conn.close()
			return render_template("busserlogin.html")

@app.route('/viewprofilebusser')
def viewprofilebusser():
			global login_user_busser
			conn = sqlite3.connect('busserprofile.db')
			print("&&&&&&&^&%%%&^^^^^^^^^^^^^^^^^^")
			print(login_user_busser)
			t=(login_user_busser,)
			cursor = conn.execute("SELECT * from Bussers WHERE Name == ? COLLATE NOCASE",t)
			return render_template("viewprofilebusser.html", rows = cursor.fetchall())

@app.route('/empviewshiftbusser')
def empviewshiftbusser():
			global login_user_busser
			conn = sqlite3.connect('bussershiftsdb.db')
			print("*********************************")
			print(login_user_busser)
			v=(login_user_busser,)
			cursor = conn.execute("SELECT * from BUSSERSHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("empviewshiftbusser.html", rows = cursor.fetchall())

@app.route('/viewpayratebusser')
def viewpayratebusser():
			global login_user_busser
			conn = sqlite3.connect('busserprofile.db')
			print("*********************************")
			print(login_user_busser)
			p=(login_user_busser,)
			cursor = conn.execute("SELECT * from Bussers WHERE Name == ? COLLATE NOCASE",p)
			return render_template("viewpayratebusser.html", rows = cursor.fetchall())

@app.route('/changeshiftsbusser')
def changeshiftsbusser():
			global login_user_busser
			conn = sqlite3.connect('bussershiftsdb.db')
			print("*********************************")
			print(login_user_busser)
			v=(login_user_busser,)
			cursor = conn.execute("SELECT * from BUSSERSHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("changeshiftsbusser.html", rows = cursor.fetchall())

@app.route('/addshiftsbusser',methods = ['POST','GET'])
def addshiftsbusser():
		global login_user_busser
		if request.method=='POST':
			fname = request.form['fna']
			role = request.form['role']
			day = request.form['daya']
			shiftstart = request.form['ssa']
			spa = request.form['spa']
			sea = request.form['sea']
			epa = request.form['epa']
			conn = sqlite3.connect('bussershiftsdb.db')
			cursor = conn.execute("SELECT * from BUSSERSHIFTS")
			for row in cursor:
				conn.execute("INSERT INTO BUSSERSHIFTS (NAME,ROLE,DAY,SHIFTSTART,SHIFTEND,STARTPERIOD,ENDPERIOD) \
					VALUES (?,?,?,?,?,?,?)",(fname, role, day,shiftstart,spa,sea,epa));
				conn.commit()
				print "Records created successfully"
				conn.close()
				return render_template("addshiftsbusser.html",name=login_user_busser)

@app.route('/deleteshiftsbusser',methods = ['POST','GET'])
def deleteshiftsbusser():
			global login_user_busser
			return render_template("deleteshiftsbusser.html",name=login_user_busser)

@app.route('/ordernotificationsbusser',methods = ['POST','GET'])
def ordernotificationsbusser():
			global login_user_busser
			return render_template("ordernotificationsbusser.html",name=login_user_busser)

@app.route('/trafficmonitoringbusser',methods = ['POST','GET'])
def trafficmonitoringbusser():
			global login_user_busser
			return render_template("trafficmonitoringbusser.html",name=login_user_busser)

if __name__ == '__main__':
    socketio.run(app)