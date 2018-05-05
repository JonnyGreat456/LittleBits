# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, render_template,request,flash
import sqlite3
from flask_socketio import SocketIO, emit
app = Flask(__name__)
# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client
app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )




login_user_chef = ""
login_user_busser = ""
login_user_waiter = ""
app.secret_key = 'some_secret'
login_user_chef_role = ""
login_user_waiter_role = ""
login_user_busser_role = ""




@app.route("/homepage")
def mainlog():
	return render_template("mainlogdemo2.html")
	
@app.route("/managerlogin")
def managerlogin():
	return render_template("managerlogin.html")
	
login_user_chef = ""

@app.route("/cheflogin")
def cheflogin():
	return render_template("cheflogin.html")
	
@app.route('/loginverifychef',methods = ['POST', 'GET'])
def loginverifychef():
	error = None
	if request.method == 'POST':
		uname = request.form['uname']
		pword = request.form['psw']
		conn = sqlite3.connect('chefprofile.db')
		cursor = conn.execute("SELECT Name,Username,Password,Row,POSITION FROM Chefs")
		for row in cursor:
			print row[1]
			print row[2]
			if(uname == row[1] and pword == row[2]):
				global login_user_chef
				global login_user_chef_role
				login_user_chef=row[0]
				login_user_chef_role = row[4]
				flash("You were successfully logged in")
				return render_template("chefmainpage.html",name=row[0])
	if request.method =='GET':
		print(login_user_chef)
		return render_template("chefmainpage.html",name=login_user_chef)
	error = "Invalid Credentials"
	return render_template('cheflogin.html',error = error)
			
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
			conn = sqlite3.connect('ChefSchedule.db')
			print("*********************************")
			print(login_user_chef)
			v=(login_user_chef,)
			cursor = conn.execute("SELECT * from Shifts WHERE NAME == ? COLLATE NOCASE",v)
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
			conn = sqlite3.connect('ChefSchedule.db')
			print("*********************************")
			print(login_user_chef)
			v=(login_user_chef,)
			cursor = conn.execute("SELECT * from Shifts WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("changeshiftschef.html", rows = cursor.fetchall())

@app.route('/addshiftschef',methods = ['POST','GET'])
def addshiftschef():
		global login_user_chef
		global login_user_chef_role
		if request.method=='POST':
			fname = login_user_chef
			role = login_user_chef_role
			day = request.form['daya']
			shiftstart = request.form['ssa']
			spa = request.form['spa']
			sea = request.form['sea']
			epa = request.form['epa']
			conn = sqlite3.connect('employeeshiftsdb.db')
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS;")
			for row in cursor:
				conn.execute("INSERT INTO EMPLOYEESHIFTS (NAME,ROLE,DAY,SHIFTSTART,SHIFTEND,STARTPERIOD,ENDPERIOD) \
					VALUES (?,?,?,?,?,?,?);",(fname, role, day,shiftstart,spa,sea,epa));
				conn.commit()
				print "Records created successfully"
				conn.close()
				return render_template("addshiftschef.html",name=login_user_chef)

@app.route('/deleteshiftschef',methods = ['POST','GET'])
def deleteshiftschef():
		global login_user_chef
		global login_user_chef_role
		if request.method=='POST':
			fname = login_user_chef
			role = login_user_chef_role
			day = request.form['dayd']
			shiftstart = request.form['ssd']
			spa = request.form['spd']
			sea = request.form['sed']
			epa = request.form['epd']
			conn = sqlite3.connect('employeeshiftsdb.db')
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS;")
			for row in cursor:
				conn.execute("DELETE FROM EMPLOYEESHIFTS WHERE (NAME=? AND ROLE=? AND DAY=? AND SHIFTSTART=? AND SHIFTEND=? AND STARTPERIOD=? AND ENDPERIOD=?);",(fname, role, day,shiftstart,spa,sea,epa))
				conn.commit()
				print "Records deleted successfully"
				conn.close()
				return render_template("deleteshiftschef.html",name=login_user_chef)

@app.route('/orderinterfacechef')			
def orderinterfacechef():
				conn = sqlite3.connect('OrderStatus.db')
				cursor = conn.execute("SELECT * from Orders;")
				return render_template("orderinterfacechef.html",rows = cursor.fetchall())	
				
@app.route('/orderupdate',methods = ['POST','GET'])
def orderupdate():
				global login_user_chef
				if request.method =='POST'or 'GET':
					tablenum = request.form['tablenum']
					quantity = request.form['quantity']
					items = request.form['items']
					print("++++++++++++")
					print(tablenum)
					print(items)
					print(quantity)
					conn = sqlite3.connect('OrderStatus.db')
					cursor = conn.execute("SELECT * from Orders")
					for row in cursor:
						conn.execute("DELETE FROM Orders WHERE (Item = ? AND TableNo = ?);",(items,tablenum))
						conn.commit()
						return render_template("orderinterfacechef.html",rows = cursor.fetchall(),name = login_user_chef)
		
			

@app.route("/busserlogin/")
def busserlogin():
	return render_template("busserlogin.html")

@app.route('/loginverifybusser',methods = ['POST', 'GET'])
def loginverifybusser():
	error = None
	if request.method == 'POST':
		uname = request.form['uname']
		pword = request.form['psw']
		conn = sqlite3.connect('busserprofile.db')
		cursor = conn.execute("SELECT Name,Username,Password,Row,POSITION FROM Bussers")
		for row in cursor:
			print row[1]
			print row[2]
			if(uname == row[1] and pword == row[2]):
				global login_user_busser
				global login_user_busser_role
				login_user_busser=row[0]
				login_user_busser_role = row[4]
				return render_template("bussermainpage.html",name=row[0])
	if request.method =='GET':
		print(login_user_busser)
		return render_template("bussermainpage.html",name=login_user_busser)
	error = "Invalid"
	return render_template('busserlogin.html',error=error)

@app.route('/viewprofilebusser')
def viewprofilebusser():
			global login_user_busser
			global login_user_busser_role
			conn = sqlite3.connect('busserprofile.db')
			print("&&&&&&&^&%%%&^^^^^^^^^^^^^^^^^^")
			print(login_user_busser)
			t=(login_user_busser,)
			cursor = conn.execute("SELECT * from Bussers WHERE Name == ? COLLATE NOCASE",t)
			return render_template("viewprofilebusser.html", rows = cursor.fetchall())

@app.route('/empviewshiftbusser')
def empviewshiftbusser():
			global login_user_busser
			conn = sqlite3.connect('BusserSchedule.db')
			print("*********************************")
			print(login_user_busser)
			v=(login_user_busser,)
			cursor = conn.execute("SELECT * from Shifts3 WHERE NAME == ? COLLATE NOCASE",v)
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
			conn = sqlite3.connect('employeeshiftsdb.db')
			print("*********************************")
			print(login_user_busser)
			v=(login_user_busser,)
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("changeshiftsbusser.html", rows = cursor.fetchall())

@app.route('/addshiftsbusser',methods = ['POST','GET'])
def addshiftsbusser():
		global login_user_busser
		global login_user_busser_role
		if request.method=='POST':
			fname = login_user_busser
			role = login_user_busser_role
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
				return render_template("addshiftsbusser.html",name=login_user_busser)

@app.route('/deleteshiftsbusser',methods = ['POST','GET'])
def deleteshiftsbusser():
		global login_user_busser
		global login_user_busser_role
		if request.method=='POST':
			fname = login_user_busser
			role = login_user_busser_role
			day = request.form['dayd']
			shiftstart = request.form['ssd']
			spa = request.form['spd']
			sea = request.form['sed']
			epa = request.form['epd']
			conn = sqlite3.connect('employeeshiftsdb.db')
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS;")
			for row in cursor:
				conn.execute("DELETE FROM EMPLOYEESHIFTS WHERE (NAME=? AND ROLE=? AND DAY=? AND SHIFTSTART=? AND SHIFTEND=? AND STARTPERIOD=? AND ENDPERIOD=?);",(fname, role, day,shiftstart,spa,sea,epa))
				conn.commit()
				print "Records deleted successfully"
				conn.close()
				return render_template("deleteshiftsbusser.html",name=login_user_busser)


@app.route('/trafficmonitoringbusser')
def trafficmonitoringbusser():
				global login_user_busser
				conn = sqlite3.connect('trafficmonitoring.db')
				cursor = conn.execute("SELECT * from Traffic")
				return render_template("trafficmonitoringb.html",rows = cursor.fetchall(),name = login_user_busser)
				
@app.route('/trafficmonitoringupdateb',methods = ['POST','GET'])
def trafficmonitoringupdateb():
				global login_user_busser
				if request.method =='POST':
					tablename = request.form['tablename']
					resname = request.form['resname']
					vacname = request.form['vacname']
					occname = request.form['occname']
					dirtyname = request.form['dirtyname']
					cleanname = request.form['cleanname']
					print("TTTTTTTTTTTTTT")
					print(tablename)
					print(resname)
					print(vacname)
					print(occname)
					print(dirtyname)
					print(cleanname)
					conn = sqlite3.connect('trafficmonitoring.db')
					cursor = conn.execute("SELECT * from Traffic")
					for row in cursor:
						conn.execute("DELETE from Traffic WHERE (Row = ? AND Reserved = ?);",(tablename,resname))
						conn.execute("INSERT INTO Traffic (Row,Reserved,Vacant,Occupied,Clean,Dirty) \
							VALUES (?,?,?,?,?,?)",(tablename,resname, vacname, occname,dirtyname,cleanname));
						conn.commit()
						return render_template("trafficmonitoringb.html",rows = cursor.fetchall(),name = login_user_busser)

				

			
			
@app.route("/waiterlogin/")
def waiterlogin():
	return render_template("waiterlogin.html")

@app.route('/loginverifywaiter',methods = ['POST', 'GET'])
def loginverifywaiter():
	error = None
	if request.method == 'POST':
		uname = request.form['uname']
		pword = request.form['psw']
		conn = sqlite3.connect('waiterprofile.db')
		cursor = conn.execute("SELECT Name,Username,Password,Row,POSITION FROM Waiters")
		for row in cursor:
			print row[1]
			print row[2]
			if(uname == row[1] and pword == row[2]):
				global login_user_waiter
				global login_user_waiter_role
				login_user_waiter=row[0]
				login_user_waiter_role = row[4]
				return render_template("waitermainpage.html",name=row[0])
	if request.method =='GET':
		print(login_user_waiter)
		return render_template("waitermainpage.html",name=login_user_waiter)
	error = "Invalid"
	return render_template('waiterlogin.html',error = error)


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
			conn = sqlite3.connect('WaiterSchedule.db')
			print("*********************************")
			print(login_user_waiter)
			v=(login_user_waiter,)
			cursor = conn.execute("SELECT * from Shifts2 WHERE NAME == ? COLLATE NOCASE",v)
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
			global login_user_waiter_role
			conn = sqlite3.connect('employeeshiftsdb.db')
			print("*********************************")
			print(login_user_waiter)
			v=(login_user_waiter,)
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS WHERE NAME == ? COLLATE NOCASE",v)
			return render_template("changeshiftswaiter.html", rows = cursor.fetchall())

@app.route('/addshiftswaiter',methods = ['POST','GET'])
def addshiftswaiter():
		global login_user_waiter
		global login_user_waiter_role
		if request.method=='POST':
			fname = login_user_waiter
			role = login_user_waiter_role
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
				return render_template("addshiftswaiter.html",name=login_user_waiter)

@app.route('/deleteshiftswaiter',methods = ['POST','GET'])
def deleteshiftswaiter():
		global login_user_waiter
		global login_user_waiter_role
		if request.method=='POST':
			fname = login_user_waiter
			role = login_user_waiter_role
			day = request.form['dayd']
			shiftstart = request.form['ssd']
			spa = request.form['spd']
			sea = request.form['sed']
			epa = request.form['epd']
			conn = sqlite3.connect('employeeshiftsdb.db')
			cursor = conn.execute("SELECT * from EMPLOYEESHIFTS;")
			for row in cursor:
				conn.execute("DELETE FROM EMPLOYEESHIFTS WHERE (NAME=? AND ROLE=? AND DAY=? AND SHIFTSTART=? AND SHIFTEND=? AND STARTPERIOD=? AND ENDPERIOD=?);",(fname, role, day,shiftstart,spa,sea,epa))
				conn.commit()
				print "Records deleted successfully"
				conn.close()
				return render_template("deleteshiftswaiter.html",name=login_user_waiter)

@app.route('/')
def chatapp():
			global login_user_waiter
			return render_template("./ChatApp.html",name=login_user_waiter)
def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )


@app.route('/trafficmonitoringwaiter')
def trafficmonitoringwaiter():
				global login_user_waiter
				conn = sqlite3.connect('trafficmonitoring.db')
				cursor = conn.execute("SELECT * from Traffic")
				return render_template("trafficmonitoring.html",rows = cursor.fetchall(),name = login_user_waiter)
				
@app.route('/trafficmonitoringupdate',methods = ['POST','GET'])
def trafficmonitoringupdate():
				global login_user_waiter
				if request.method =='POST'or 'GET':
					tablename = request.form['tablename']
					resname = request.form['resname']
					vacname = request.form['vacname']
					occname = request.form['occname']
					dirtyname = request.form['dirtyname']
					cleanname = request.form['cleanname']
					print("TTTTTTTTTTTTTT")
					print(tablename)
					print(resname)
					print(vacname)
					print(occname)
					print(dirtyname)
					print(cleanname)
					conn = sqlite3.connect('trafficmonitoring.db')
					cursor = conn.execute("SELECT * from Traffic")
					for row in cursor:
						conn.execute("DELETE from Traffic WHERE Row = ?",tablename)
						conn.execute("INSERT INTO Traffic (Row,Reserved,Vacant,Occupied,Clean,Dirty) \
							VALUES (?,?,?,?,?,?)",(tablename,resname, vacname, occname,dirtyname,cleanname));
						conn.commit()
						return render_template("trafficmonitoring.html",rows = cursor.fetchall(),name = login_user_waiter)

				
if __name__ == '__main__':
    socketio.run( app, debug = True )