# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import math 
import sqlite3 as sql
import numpy as np

app = Flask(__name__)

@app.route('/')
def mainmenu1():
   return render_template('mainmenu1.html')

@app.route('/inventorymenu1')
def inventorymenu1():
    return render_template('inventorymenu1.html')

@app.route('/financemenu1')
def financemenu1():
    return render_template('financemenu1.html')

@app.route('/profitMenu')
def profitMenu():
    return render_template('profitMenu.html')

@app.route('/employeePortal1')
def employeePortal1():
    return render_template('employeePortal1.html')

@app.route('/weeklyProfits')
def weeklyProfits():
    #transactionDict = {'26MAR18': -10805.35}
    con = sql.connect("transactionHistory.db")
    cursor = con.execute("SELECT * FROM transactions")
    records = cursor.fetchall()
    transactionDict = {records[0][2]:records[0][3]}
    for record in records:
        date = record[2]
        inDatabase = False
        for key in transactionDict:
            if(key == date):
                transactionDict[key] += record[3]
                inDatabase = True
        if(inDatabase == False):
            transactionDict[date] = record[3]
    
    return render_template("weeklyProfits.html", rows = transactionDict)

@app.route('/menuUpdated')
def updateMenuItem():
    return render_template('updateMenuItem.html')

@app.route('/addItemForm')
def addItemForm():
    return render_template('addItemForm.html')

@app.route('/profProjForm')
def profProjForm():
    return render_template('profProjForm.html')

@app.route('/result5')
def projectProfits():
    return render_template('result5.html')

@app.route('/deleteItemForm')
def deleteItemForm():
    return render_template('deleteItemForm.html')

@app.route('/addEmployee1')
def addEmployee1():
    return render_template('addEmployee1.html')

@app.route('/deleteEmployee1')
def deleteEmployee1():
    return render_template('deleteEmployee1.html')

@app.route('/searchInventory')
def searchInventory():
    return render_template('searchInventory.html')

@app.route('/updateInventory1', methods = ['POST', 'GET'])
def searchInv():
    msg = ""
    if(request.method == 'POST'):
        try:
            nm = request.form['nm']
            exp = request.form['exp']
            con = sql.connect('inventory.db')
            cursor = con.execute("SELECT * FROM inventory WHERE (itemName = ? AND expirationDate = ?);",(nm,exp))
            con.execute("DELETE FROM inventory WHERE (itemName = ? AND expirationDate = ?);",(nm,exp))
            con.commit()
            msg = "Record successfully found"
        except:
            con.rollback()
            msg = "error in search operation"
        finally:
            return render_template("updateInventory1.html", msg = msg, rows = cursor.fetchall())

@app.route('/updateResult', methods = ['POST', 'GET'])
def updInv():
    msg = ""
    if(request.method == 'POST'):
        try:
            nm = request.form['nm']
            qua = request.form['qua']
            uom = request.form['uom']
            exp = request.form['exp']
            cpu = request.form['cpu']
            expF = 0
            con = sql.connect('inventory.db')
            con.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
             VALUES (?,?,?,?,?,?);",(nm,qua,uom,exp,cpu,expF))
            con.commit()
            msg = "Record successfully updated"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("updateResult.html", msg = msg)

@app.route('/restaurantTraffic1')
def restaurantTraffic1():
    return render_template('restaurantTraffic1.html')

@app.route('/inventoryPage')
def inventoryPage():
   con = sql.connect("inventory.db")
   cursor = con.execute("SELECT itemName, quantity, unitOfMeasure, expirationDate, costPerUnit FROM inventory")
   return render_template("inventoryPage.html", rows = cursor.fetchall())

@app.route('/result', methods = ['POST', 'GET'])
def addInv():
    msg = ""
    if(request.method == 'POST'):
        try:
            nm = request.form['nm']
            qua = request.form['qua']
            uom = request.form['uom']
            exp = request.form['exp']
            cpu = request.form['cpu']
            expF = 0
            con = sql.connect('inventory.db')
            con.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
             VALUES (?,?,?,?,?,?);",(nm,qua,uom,exp,cpu,expF))
            con.commit()
            msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result.html", msg = msg)


@app.route('/result2', methods = ['POST', 'GET'])
def delInv():
    msg = ""
    if(request.method == 'POST'):
        try:
            nm = request.form['nm']
            exp = request.form['exp']
            con = sql.connect('inventory.db')
            con.execute("DELETE FROM inventory WHERE (itemName = ? AND expirationDate = ?);",(nm,exp))
            con.commit()
            msg = "Record successfully deleted"
        except:
            con.rollback()
            msg = "error in delete operation"
        finally:
            return render_template("result2.html", msg = msg)

			
x = []
y = []
z = []
@app.route('/result6', methods = ['POST', 'GET'])
def displayProjection():
	if(request.method == 'POST'):
		days = request.form['timeframe']
		con = sql.connect("transactionHistory.db")
		cursor = con.execute("SELECT * FROM transactions")
		records = cursor.fetchall()
		transactionDict = {records[0][2]:records[0][3]}
		for record in records:
			date = record[2]
			inDatabase = False
			for key in transactionDict:
				if(key == date):
					transactionDict[key] += record[3]
					inDatabase = True
			if(inDatabase == False):
				transactionDict[date] = record[3]
		transactions = []
		for k,v in transactionDict.items(): 
			transactions.append([k, v]) 
		i = 0
		for p in transactions:
			x.append(i)
			i += 1
		for m in transactions:
			y.append(m[1])
		coeff = np.polyfit(x,y,3)
		for c in coeff:
			z.append(round(c))
        return render_template('result6.html', dictionary = transactions, numbers = z, xaxis = x, days = days)

@app.route('/deleted', methods = ['POST', 'GET'])
def delMenu():
	print("Good\n")
	msg = ""
	if(request.method == 'POST'):
		try:
			print("Good\n")
			cat = request.form['cat']
			nme = request.form['nme']
			con = sql.connect('menu.db')
			print("Good\n")
			con.execute("DELETE FROM menu WHERE (category=? AND itemName=?);",(cat,nme))
			con.commit()
			print("Good\n")
			msg = "Menu item successfully deleted"
		except:
		    con.rollback()
		    msg = "error in deleting menu operation"
		finally:
		    return render_template("deleted.html", msg = msg)

@app.route('/added', methods = ['POST', 'GET'])
def addMenu():
    print("Good\n")
    msg = ""
    if(request.method == 'POST'):
        try:
            print("Good\n")
            cat = request.form['cat']
            nme = request.form['nme']
            pri = request.form['pri']
            lir = ''
            ing = request.form['ing']
            qua = request.form['qua']
            uom = request.form['uom']
            con = sql.connect('menu.db')
            cursor = con.execute('SELECT * FROM menu WHERE ID = (SELECT MAX(ID) FROM menu);')
            record = cursor.fetchall()
            row = record[0][0] + 1
            con.execute("INSERT INTO menu (ID, category, itemName, itemPrice,listRatings, ingredientName, quantity, unitOfMeasure) \
             VALUES (?,?,?,?,?,?,?,?);",(row,cat,nme,pri,lir,ing,qua,uom))
            con.commit()
            print("Good\n")
            msg = "Menu item successfully added"
        except:
            con.rollback()
            msg = "error in inserting menu operation"
        finally:
            return render_template("added.html", msg = msg)

@app.route('/updatedMenu', methods=['POST','GET'])
def updMenu():
    print("Works\n")
    msg=""
    if(request.method =='POST'):
        try:
            print("Updating\n")
            pri = request.form['pri']
            cat = request.form['cat']
            nme = request.form['nme']
            con = sql.connect('menu.db')
            con.execute("UPDATE menu SET itemPrice=? WHERE (category=? AND itemName=?);",(pri,cat,nme))
            con.commit()
            print("Updated\n")
            msg = "Menu item successfully updated"
        except:
            con.rollback()
            msg = "Error in updating menu item"
        finally:
            return render_template("updatedMenu.html", msg= msg)

@app.route('/result3', methods = ['POST', 'GET'])
def addEmp():
    msg = ""
    if(request.method == 'POST'):
        try:
            name = request.form['name']
            pos = request.form['role']
            dob = request.form['dob']
            phone = request.form['phone']
            uname = request.form['uname']
            pword = request.form['pword']
            pay = 0
            if(pos == "Manager"):
                pay = 25
            elif(pos == "Busser"):
                pay = 9
            elif(pos == "Waiter"):
                pay = 12
            elif(pos == "Chef"):
                pay = 18
            con = sql.connect('StaffProfile.db')
            cursor = con.execute('SELECT * FROM Profile WHERE Row = (SELECT MAX(Row) FROM Profile);')
            record = cursor.fetchall()
            row = record[0][0] + 1
            con.execute("INSERT INTO Profile (Row, Name, Position, DOB, Phone, Pay, Username, Password) \
             VALUES (?,?,?,?,?,?,?,?);",(row,name,pos,dob,phone,pay,uname,pword))
            con.commit()
            msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result3.html", msg = msg)

@app.route('/result4', methods = ['POST', 'GET'])
def delEmp():
    msg = ""
    if(request.method == 'POST'):
        try:
            nm = request.form['name']
            con = sql.connect('StaffProfile.db')
            statement = 'DELETE FROM Profile WHERE Name=?;'
            cur = con.cursor()
            cur.execute(statement, (nm,))
            con.commit()
            msg = "Record successfully deleted"
        except:
            con.rollback()
            msg = "error in delete operation"
        finally:
            return render_template("result4.html", msg = msg)

@app.route('/menuoptions1')
def menuoptions1():
    return render_template("menuoptions1.html")

@app.route('/addtoMenu')
def addtoMenu():
    return render_template("addtoMenu.html")

@app.route('/deleteFromMenu')
def deleteFromMenu():
    return render_template("deleteFromMenu.html")

@app.route('/menuPage')
def menuPage():
    con=sql.connect("menu.db")
    ex = con.execute("SELECT ID,category, itemName, itemPrice,listRatings,ingredientName,quantity,unitOfMeasure FROM menu")
    return render_template("menuPage.html", rows = ex.fetchall())

@app.route('/transactionsTable')
def transactionsTable():
    con = sql.connect("transactionHistory.db")
    cursor = con.execute("SELECT ID, DETAILS, TRANSACTION_DATE, COST FROM transactions;")
    return render_template("transactionsTable.html", rows = cursor.fetchall())

@app.route('/wagesPage')
def wagesPage():
    con = sql.connect("StaffProfile.db")
    cursor = con.execute("SELECT Name, Position, Pay FROM Profile;")
    return render_template("wagesPage.html", rows = cursor.fetchall())

@app.route('/buttonresult1')
def buttonresult1():
    return render_template("buttonresult1.html")

if(__name__ == "__main__"):
   app.run(host = 'localhost',port = 8000,debug = True)
