# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__)
login_user = ""
@app.route("/")
def mainlog():
	return render_template("mainlog.html")
  
@app.route("/employeelogin/")
def employeelogin():
	return render_template("employeelogin.html")
	
@app.route("/managerlogin")
def managerlogin():
	return render_template("managerlogin.html")
	
@app.route('/loginverify',methods = ['POST', 'GET'])
def loginverify():
	if request.method == 'POST':
		uname = request.form['uname']
		pword = request.form['psw']
		conn = sqlite3.connect('employeeprofile.db')
		cursor = conn.execute("SELECT Name,Username,Password,Row FROM Employees")
		for row in cursor:
			print row[1]
			print row[2]
			if(uname == row[1] and pword == row[2]):
				global login_user
				login_user=row[0]
				return render_template("employeemainpage.html",name=row[0])
	if request.method =='GET':
		print(login_user)
		return render_template("employeemainpage.html",name=login_user)
	return render_template('employeelogin.html')

@app.route('/signup',methods = ['POST','GET'])
def signup():
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
		
		conn = sqlite3.connect('employeeprofile.db')
		cursor = conn.execute("SELECT Name,POSITION,DOB,Phone,Pay,Username,Password from Employees")
		for row in cursor:
			conn.execute("INSERT INTO Employees (Row,Name,POSITION,DOB,Phone,Pay,Username,Password) \
				VALUES (NULL,?,?,?,?,?,?,?)",(fullname, position, dob,phone_number,pay,uname,pword));
			conn.commit()
			print "Records created successfully"
			conn.close()
			return render_template("employeelogin.html")

@app.route('/viewprofile')
def viewprofile():
			global login_user
			conn = sqlite3.connect('employeeprofile.db')
			print("&&&&&&&^&%%%&^^^^^^^^^^^^^^^^^^")
			print(login_user)
			t=(login_user,)
			cursor = conn.execute("SELECT * from Employees WHERE Name == ? COLLATE NOCASE",t)
			return render_template("viewprofile.html", rows = cursor.fetchall())
			
@app.route('/empviewshift')
def empviewshift():
			global login_user
			conn = sqlite3.connect('employeeshiftsdb.db')
			print("*********************************")
			print(login_user)
			v=(login_user,)
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("empviewshift.html", rows = cursor.fetchall())
@app.route('/viewpayrate')
def viewpayrate():
			global login_user
			conn = sqlite3.connect('employeeprofile.db')
			print("*********************************")
			print(login_user)
			p=(login_user,)
			cursor = conn.execute("SELECT * from Employees WHERE Name == ? COLLATE NOCASE",p)
			return render_template("viewpayrate.html", rows = cursor.fetchall())

@app.route('/changeshifts')
def changeshifts():
			global login_user
			conn = sqlite3.connect('employeeshiftsdb.db')
			print("*********************************")
			print(login_user)
			v=(login_user,)
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("changeshifts.html", rows = cursor.fetchall())

@app.route('/addshifts',methods = ['POST','GET'])
def addshifts():
		global login_user
		if request.method=='POST':
			fname = request.form['fna']
			role = request.form['role']
			day = request.form['daya']
			shiftstart = request.form['ssa']
			spa = request.form['spa']
			sea = request.form['sea']
			epa = request.form['epa']
			conn = sqlite3.connect('employeeshiftsdb.db')
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS")
			for row in cursor:
				conn.execute("INSERT INTO EMPLOYEESHIFTS (NAME,ROLE,DAY,SHIFTSTART,SHIFTEND,STARTPERIOD,ENDPERIOD) \
					VALUES (?,?,?,?,?,?,?)",(fname, role, day,shiftstart,spa,sea,epa));
				conn.commit()
				print "Records created successfully"
				conn.close()
				return render_template("addshifts.html",name=login_user)

@app.route('/deleteshifts',methods = ['POST','GET'])
def deleteshifts():
			global login_user
			return render_template("lo.html,name=login_user")

@app.route('/orderstatus')			
def orderstatus():
			conn = sqlite3.connect('OrderStatus.db')
			cursor = conn.execute("SELECT * from Orders")
			return render_template("orderstatus.html",rows = cursor.fetchall())


		
app.run(debug = True)