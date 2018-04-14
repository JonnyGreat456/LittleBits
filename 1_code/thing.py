# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import math 
import sqlite3 as sql 

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

@app.route('/addItemForm')
def addItemForm():
    return render_template('addItemForm.html')

@app.route('/deleteItemForm')
def deleteItemForm():
    return render_template('deleteItemForm.html')

@app.route('/menuUpdated')
def updateMenuItem():
    return render_template('updateMenuItem.html')

@app.route('/inventoryPage')
def inventoryPage():
   con = sql.connect("inventory.db")
   cursor = con.execute("SELECT itemName, quantity, unitOfMeasure, expirationDate, costPerUnit FROM inventory")
   return render_template("inventoryPage.html", rows = cursor.fetchall())

@app.route('/menuPage')
def menuPage():
    con=sql.connect("menu.db")
    ex = con.execute("SELECT category, itemName, itemPrice,listRatings,ingredientName,quantity,unitOfMeasure FROM menu")
    return render_template("menuPage.html", rows = ex.fetchall())

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
    print("here\n")
    if(request.method == 'POST'):
        try:
            print("here\n")
            nm = request.form['nm']
            exp = request.form['exp']
            con = sql.connect('inventory.db')
            print("here\n")
            con.execute("DELETE FROM inventory WHERE (itemName = ? AND expirationDate = ?);",(nm,exp))
            print("here\n")
            con.commit()
            msg = "Record successfully deleted"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result2.html", msg = msg)


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
            print("Good\n")
            con.execute("INSERT INTO menu (category, itemName, itemPrice,listRatings, ingredientName, quantity, unitOfMeasure) \
             VALUES (?,?,?,?,?,?,?);",(cat,nme,pri,lir,ing,qua,uom))
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
            cat = request.form['cat']
            nme = request.form['nme']
            pri = request.form['pri']
            con = sql.connect('menu.db')
            con.execute("UPDATE menu SET itemPrice=pri WHERE (category=? AND itemName=?);"(cat,nme))
            con.commit()
            print("Updated\n")
            msg = "Menu item successfully updated"
        except:
            con.rollback()
            msg = "Error in updating menu item"
        finally:
            return render_template("updatedMenu.html", msg= msg)

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

@app.route('/menuoptions1')
def menuoptions1():
    return render_template("menuoptions1.html")

@app.route('/addtoMenu')
def addtoMenu():
    return render_template("addtoMenu.html")

@app.route('/deleteFromMenu')
def deleteFromMenu():
    return render_template("deleteFromMenu.html")

@app.route('/transactionsTable')
def transactionsTable():
    return render_template("transactionsTable.html")

@app.route('/wagesPage')
def wagesPage():
    return render_template("wagesPage.html")

@app.route('/buttonresult1')
def buttonresult1():
    return render_template("buttonresult1.html")

if(__name__ == "__main__"):
   app.run(debug = True)
