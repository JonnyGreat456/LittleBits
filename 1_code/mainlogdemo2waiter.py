# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, render_template,request
from flask_socketio import SocketIO,emit
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

login_user_waiter = ""

@app.route("/waiterlogin/")
def waiterlogin():
	return render_template("waiterlogin.html")

@app.route('/loginverifywaiter',methods = ['POST', 'GET'])
def loginverifywaiter():
	if request.method == 'POST':
		uname = request.form['uname']
		pword = request.form['psw']
		conn = sqlite3.connect('waiterprofile.db')
		cursor = conn.execute("SELECT Name,Username,Password,Row FROM Waiters")
		for row in cursor:
			print row[1]
			print row[2]
			if(uname == row[1] and pword == row[2]):
				global login_user_waiter
				login_user_waiter=row[0]
				return render_template("waitermainpage.html",name=row[0])
	if request.method =='GET':
		print(login_user_waiter)
		return render_template("waitermainpage.html",name=login_user_waiter)
	return render_template('waiterlogin.html')

@app.route('/signupwaiter',methods = ['POST','GET'])			
def signupwaiter():
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
		
		conn = sqlite3.connect('waiterprofile.db')
		cursor = conn.execute("SELECT Name,POSITION,DOB,Phone,Pay,Username,Password from Waiters")
		for row in cursor:
			conn.execute("INSERT INTO Waiters (Row,Name,POSITION,DOB,Phone,Pay,Username,Password) \
				VALUES (NULL,?,?,?,?,?,?,?)",(fullname, position, dob,phone_number,pay,uname,pword));
			conn.commit()
			print "Records created successfully"
			conn.close()
			return render_template("waiterlogin.html")

@app.route('/viewprofilewaiter')
def viewprofilewaiter():
			global login_user_waiter
			conn = sqlite3.connect('waiterprofile.db')
			print("&&&&&&&^&%%%&^^^^^^^^^^^^^^^^^^")
			print(login_user_waiter)
			t=(login_user_waiter,)
			cursor = conn.execute("SELECT * from Waiters WHERE Name == ? COLLATE NOCASE",t)
			return render_template("viewprofilewaiter.html", rows = cursor.fetchall())
			
@app.route('/empviewshiftwaiter')
def empviewshiftwaiter():
			global login_user_waiter
			conn = sqlite3.connect('waitershiftsdb.db')
			print("*********************************")
			print(login_user_waiter)
			v=(login_user_waiter,)
			cursor = conn.execute("SELECT * from WAITERSHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("empviewshiftwaiter.html", rows = cursor.fetchall())

@app.route('/viewpayratewaiter')
def viewpayratewaiter():
			global login_user_waiter
			conn = sqlite3.connect('waiterprofile.db')
			print("*********************************")
			print(login_user_waiter)
			p=(login_user_waiter,)
			cursor = conn.execute("SELECT * from Waiters WHERE Name == ? COLLATE NOCASE",p)
			return render_template("viewpayratewaiter.html", rows = cursor.fetchall())

@app.route('/changeshiftswaiter')
def changeshiftswaiter():
			global login_user_waiter
			conn = sqlite3.connect('waitershiftsdb.db')
			print("*********************************")
			print(login_user_waiter)
			v=(login_user_waiter,)
			cursor = conn.execute("SELECT * from WAITERSHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("changeshiftswaiter.html", rows = cursor.fetchall())

@app.route('/addshiftswaiter',methods = ['POST','GET'])
def addshiftswaiter():
		global login_user_waiter
		if request.method=='POST':
			fname = request.form['fna']
			role = request.form['role']
			day = request.form['daya']
			shiftstart = request.form['ssa']
			spa = request.form['spa']
			sea = request.form['sea']
			epa = request.form['epa']
			conn = sqlite3.connect('waitershiftsdb.db')
			cursor = conn.execute("SELECT * from WAITERSHIFTS")
			for row in cursor:
				conn.execute("INSERT INTO WAITERSHIFTS (NAME,ROLE,DAY,SHIFTSTART,SHIFTEND,STARTPERIOD,ENDPERIOD) \
					VALUES (?,?,?,?,?,?,?)",(fname, role, day,shiftstart,spa,sea,epa));
				conn.commit()
				print "Records created successfully"
				conn.close()
				return render_template("addshiftswaiter.html",name=login_user_waiter)

@app.route('/deleteshiftswaiter',methods = ['POST','GET'])
def deleteshiftswaiter():
			global login_user_waiter
			return render_template("deleteshiftswaiter.html",name=login_user_waiter)

@app.route('/ordernotificationswaiter',methods = ['POST','GET'])
def ordernotificationswaiter():
			global login_user_waiter
			return render_template("ordernotificationswaiter.html",name=login_user_waiter)

@app.route('/trafficmonitoringwaiter',methods = ['POST','GET'])
def trafficmonitoringwaiter():
			global login_user_waiter
			return render_template("trafficmonitoringwaiter.html",name=login_user_waiter)

if __name__ == '__main__':
    socketio.run(app)

