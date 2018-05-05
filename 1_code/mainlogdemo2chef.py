# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, render_template,request
from flask_socketio import SocketIO,emit
import sqlite3

app = Flask(__name__)

login_user_chef = ""


	
@app.route("/cheflogin")
def cheflogin():
	return render_template("cheflogin.html")
	
@app.route('/loginverifychef',methods = ['POST', 'GET'])
def loginverifychef():
	if request.method == 'POST':
		uname = request.form['uname']
		pword = request.form['psw']
		conn = sqlite3.connect('chefprofile.db')
		cursor = conn.execute("SELECT Name,Username,Password,Row FROM Chefs")
		for row in cursor:
			print row[1]
			print row[2]
			if(uname == row[1] and pword == row[2]):
				global login_user_chef
				login_user_chef=row[0]
				return render_template("chefmainpage.html",name=row[0])
	if request.method =='GET':
		print(login_user_chef)
		return render_template("chefmainpage.html",name=login_user_chef)
	return render_template('cheflogin.html')

def signupchef():
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
		
		conn = sqlite3.connect('chefprofile.db')
		cursor = conn.execute("SELECT Name,POSITION,DOB,Phone,Pay,Username,Password from Chefs")
		for row in cursor:
			conn.execute("INSERT INTO Chefs (Row,Name,POSITION,DOB,Phone,Pay,Username,Password) \
				VALUES (NULL,?,?,?,?,?,?,?)",(fullname, position, dob,phone_number,pay,uname,pword));
			conn.commit()
			print "Records created successfully"
			conn.close()
			return render_template("cheflogin.html")

@app.route('/viewprofilechef')
def viewprofilechef():
			global login_user_chef
			conn = sqlite3.connect('chefprofile.db')
			print("&&&&&&&^&%%%&^^^^^^^^^^^^^^^^^^")
			print(login_user_chef)
			t=(login_user_chef,)
			cursor = conn.execute("SELECT * from Chefs WHERE Name == ? COLLATE NOCASE",t)
			return render_template("viewprofilechef.html", rows = cursor.fetchall())
			
@app.route('/empviewshiftchef')
def empviewshiftchef():
			global login_user_chef
			conn = sqlite3.connect('chefshiftsdb.db')
			print("*********************************")
			print(login_user_chef)
			v=(login_user_chef,)
			cursor = conn.execute("SELECT * from CHEFSHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("empviewshiftchef.html", rows = cursor.fetchall())

@app.route('/viewpayratechef')
def viewpayratechef():
			global login_user_chef
			conn = sqlite3.connect('chefprofile.db')
			print("*********************************")
			print(login_user_chef)
			p=(login_user_chef,)
			cursor = conn.execute("SELECT * from Chefs WHERE Name == ? COLLATE NOCASE",p)
			return render_template("viewpayratechef.html", rows = cursor.fetchall())

@app.route('/changeshiftschef')
def changeshiftschef():
			global login_user_chef
			conn = sqlite3.connect('chefshiftsdb.db')
			print("*********************************")
			print(login_user_chef)
			v=(login_user_chef,)
			cursor = conn.execute("SELECT * from CHEFSHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("changeshiftschef.html", rows = cursor.fetchall())

@app.route('/addshiftschef',methods = ['POST','GET'])
def addshiftschef():
		global login_user_chef
		if request.method=='POST':
			fname = request.form['fna']
			role = request.form['role']
			day = request.form['daya']
			shiftstart = request.form['ssa']
			spa = request.form['spa']
			sea = request.form['sea']
			epa = request.form['epa']
			conn = sqlite3.connect('chefshiftsdb.db')
			cursor = conn.execute("SELECT * from CHEFSHIFTS")
			for row in cursor:
				conn.execute("INSERT INTO CHEFSHIFTS (NAME,ROLE,DAY,SHIFTSTART,SHIFTEND,STARTPERIOD,ENDPERIOD) \
					VALUES (?,?,?,?,?,?,?)",(fname, role, day,shiftstart,spa,sea,epa));
				conn.commit()
				print "Records created successfully"
				conn.close()
				return render_template("addshiftschef.html",name=login_user_chef)

@app.route('/deleteshiftschef',methods = ['POST','GET'])
def deleteshiftschef():
			global login_user_chef
			return render_template("deleteshiftschef.html",name=login_user_chef)

@app.route('/orderinterfacechef')			
def orderinterfacechef():
			conn = sqlite3.connect('OrderStatus.db')
			cursor = conn.execute("SELECT * from Orders")
			return render_template("orderinterfacechef.html",rows = cursor.fetchall())
