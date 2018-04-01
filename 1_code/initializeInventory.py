# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import math 
import sqlite3 as sql 

app = Flask(__name__)

conn = sql.connect('inventory.db')

print("Database opened successfully...")

conn.execute('''DROP TABLE IF EXISTS inventory;''')

conn.execute('''CREATE TABLE inventory (
    itemName TEXT NOT NULL,
    quantity FLOAT NOT NULL,
    unitOfMeasure TEXT NOT NULL,
    expirationDate TEXT NOT NULL,
    costPerUnit FLOAT NOT NULL,
    expireFlag INTEGER NOT NULL
);''')

print("Table created successfully..." + "\n")

# Dessert
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Lava Cake', 29.9, 'lbs', '2019-01-11', 4.18, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Vanilla Ice Cream', 40.0, 'lbs', '2018-09-19', 1.00, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Chocolate Ice Cream', 40.0, 'lbs', '2018-09-19', 1.11, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Apple Pie', 131.25, 'lbs', '2019-03-29', 2.28, 0);")

# Appetizer
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Spinach Dip', 5.0, 'lbs', '2018-04-10', 4.99, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Potatoes', 60.0, 'lbs', '2018-06-30', 0.46, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frying Oil', 100.0, 'gal', '2018-06-01', 4.17, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Chicken Wings', 100.0, 'lbs', '2018-11-30', 4.02, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Celery', 100.0, 'lbs', '2018-04-20', 1.49, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Mozzarella Sticks', 72.0, 'lbs', '2018-09-30', 5.58, 0);")

conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Barbeque Sauce', 150.0, 'lbs', '2019-04-30', 3.79, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Ranch Dressing', 32.0, 'gal', '2018-05-11', 10.99, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Buffalo Sauce', 150.0, 'gal', '2019-04-23', 12.99, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Blue Cheese', 60.0, 'gal', '2018-12-30', 16.80, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Marinara Sauce', 60.0, 'lbs', '2018-04-09', 3.20, 0);")

# Kid's Menu
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Chicken Nuggets', 100.0, 'lbs', '2018-11-29', 5.11, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen French Fries', 210.0, 'lbs', '2018-11-12', 2.01, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Cheese Pizza', 50.0, 'lbs', '2018-04-10', 8.83, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Pepperoni', 50.0, 'lbs', '2018-11-30', 4.73, 0);")

# Drinks
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Tea Bags', 60.0, 'lbs', '2019-04-30', 3.24, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Coca Cola Syrup', 75.0, 'gal', '2018-07-21', 19.19, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Sprite Syrup', 75.0, 'gal', '2018-07-21', 16.72, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Coffee Beans', 500.0, 'lbs', '2020-04-30', 7.95, 0);")

# Pasta 
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Lasagne', 112.0, 'lbs', '2019-04-30', 3.06, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Macaroni Shells', 200.0, 'lbs', '2019-07-21', 0.50, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Parmesean Cheese', 110.0, 'lbs', '2018-05-21', 6.38, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Mozzarella Cheese', 150.0, 'lbs', '2018-05-21', 3.06, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Ravioli', 66.0, 'lbs', '2018-07-15', 7.94, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Canned Alfredo Sauce', 80.0, 'lbs', '2018-06-25', 4.25, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen Chicken Tenders', 112.0, 'lbs', '2018-09-15', 7.09, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Penne Pasta Shells', 200.0, 'lbs', '2019-07-15', 0.54, 0);")


# Soup
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Canned Chili without Beans', 160.0, 'lbs', '2021-07-15', 2.92, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Beef Broth', 120.0, 'lbs', '2019-07-15', 2.03, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Frozen White Bread Dough', 82.6, 'lbs', '2018-09-15', 1.68, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Yellow Onions', 50.0, 'lbs', '2018-05-15', 0.52, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Canned Tomato Soup', 122.0, 'lbs', '2020-07-15', 0.66, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Croutons', 96.0, 'lbs', '2018-09-17', 3.95, 0);")

# Sides
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Tomatoes', 40.0, 'lbs', '2018-04-11', 2.25, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Cucumber', 30.0, 'lbs', '2018-04-15', 2.40, 0);")
conn.execute("INSERT INTO inventory (itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag) \
      VALUES ('Italian Dressing', 72.0, 'gal', '2018-06-23', 6.09, 0);")

print("Elements inserted successfully..." + "\n")

conn.commit()
cursor = conn.execute("SELECT itemName, quantity, unitOfMeasure, expirationDate, costPerUnit, expireFlag from inventory;")
for row in cursor:
   print("ITEM_NAME = " + row[0])
   print("QUANTITY = " + str(row[1]))
   print("UNIT_OF_MEASURE = " + row[2])
   print("EXPIRATION_DATE = " + row[3])
   print("COST_PER_UNIT = " + str(row[4]))
   print("EXPIRE_FLAG = " + str(row[5]) + "\n")

print("Operation done successfully" + "\n")

conn.close()

print("Database closed successfully." + "\n")
