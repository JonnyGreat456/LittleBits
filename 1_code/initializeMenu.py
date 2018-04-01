# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import math 
import sqlite3 as sql 

app = Flask(__name__)

conn = sql.connect('Menu.db')

print("Database opened successfully...")

conn.execute('''DROP TABLE IF EXISTS Menu;''')

conn.execute('''CREATE TABLE Menu (
    category TEXT NOT NULL,
    itemName TEXT NOT NULL,
    itemPrice FLOAT NOT NULL,
    listRatings TEXT NOT NULL,
    ingredientName TEXT NOT NULL, 
    quantity FLOAT NOT NULL,
    unitOfMeasure TEXT NOT NULL
);''')

print("Table created successfully..." + "\n")

# Dessert
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Dessert', 'Lava Cake', 4.75, '4.3,3.4,4.4,', 'Lava Cake', 0.63, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Dessert', 'Vanilla Ice Cream', 3.50, '3.7,4.0', 'Vanilla Ice Cream', 0.65, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Dessert', 'Chocolate Ice Cream', 3.50, '3.6,3.8', 'Chocolate Ice Cream', 0.65, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Dessert', 'Apple Pie', 4.25, '4.3,4.2', 'Apple Pie', 0.85, 'lbs');")

# Appetizer
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Appetizer', 'Spinach Dip', 3.25, '3.2,3.6,2.9', 'Spinach Dip', 0.7, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Appetizer', 'Stuffed Potatoe Skins', 5.00, '3.8,3.8', 'Potatoes', 1.00, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Appetizer', 'Buffalo Wings', 6.75, '4.1,3.4,3.7', 'Frozen Chicken Wings', 0.5, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Appetizer', 'Celery', 100.0, 'lbs', '2018-04-20', 1.49, 0);")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Appetizer', 'Mozzarella Sticks', 4.50, '4.8,4.3,4.2,4.9', 'Frozen Mozzarella Sticks', 0.45, 'lbs');")

# Kid's Menu
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Kids Menu', 'Chicken Nuggets', 5.25, '5.0,4.9,5.0', 'Frozen Chicken Nuggets', 0.78, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Kids Menu', 'French Fries', 2.50, '3.8,3.9,4.1', 'Frozen French Fries', 0.4, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Kids Menu', 'Cheese Pizza', 5.00, 'lbs', 'Frozen Cheese Pizza', 1.25, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Kids Menu', 'Pepperoni Pizza', 5.25, '3.4,3.5,3.2', 'Pepperoni', 1.25, 'lbs');")

# Drinks
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Drinks', 'Tea', 2.55, '3.4', 'Tea Bags', 0.007, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Drinks', 'Coca Cola', 2.25, '3.7,2.5', 'Coca Cola Syrup', 0.09, 'gal');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Drinks', 'Sprite', 2.25, '3.8,4.1', 'Sprite Syrup', 0.09, 'gal');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Drinks', 'Coffee', 2.55, '3.8,2.9,4.6,4.1', 'Coffee Beans', 0.057, 'lbs');")

# Pasta 
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Pasta', 'Lasagne', 12.25, '3.7,3.8,3.7', 'Frozen Lasagne', 0.58, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Pasta', 'Macaroni and Cheese', 10.50, '4.3,4.1', 'Macaroni Shells', 1.00, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Pasta', 'Chicken Parmesan', 15.75, '4.3,4.5,3.7', 'Mozzarella Cheese', 0.19, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Pasta', 'Ravioli', 11.75, '3.2,2.9,3.8', 'Frozen Ravioli', 1.15, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Pasta', 'Alfredo Pasta', 13.25, '3.4,3.2', 'Canned Alfredo Sauce', 0.33, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Pasta', 'Chicken Tenders', 10.25, '3.5,4.1', 'Frozen Chicken Tenders', 0.91, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Pasta', 'Penne Pasta', 12.75, '4.1,4.3,4.3', 'Penne Pasta Shells', 1.25, 'lbs');")


# Soup
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Soup', 'Canned Chili', 8.75, '3.3,3.0,4.0', 'Canned Chili without Beans', 0.75, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Soup', 'Beef and Vegetable soup', 8.95, '3.2,2.9,3.5', 'Beef Broth', 0.65, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Soup', 'French Onion Soup', 8.50, '4.2,4.3,3.7', 'Yellow Onions', 0.52, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Soup', 'Tomato Soup', 8.25, '1.5,3.4,2.6,3.8,2.5', 'Canned Tomato Soup', 0.75, 'lbs');")


# Sides
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Sides', 'House Salad with Italian Dressing', 3.00, '3.2,4.1,3.7', 'Italian Dressing', 0.5, 'lbs');")
conn.execute("INSERT INTO Menu (category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES ('Sides', 'Cesar Salad', 2.75, '3.4,2.6,3.0,2.9', 'Croutons', 0.09, 'lbs');")
print("Elements inserted successfully..." + "\n")

conn.commit()
cursor = conn.execute("SELECT category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure from Menu;")
for row in cursor:
   print("CATEGORY = " + (row[0]))
   print("ITEM_NAME = " + (row[1]))
   print("ITEM_PRICE = " + str(row[2]))
   print("LIST_OF_RATINGS = " + (row[3]))
   print("INGREDIENT_NAME = " + (row[4]))
   print("QUANTITY = " + str(row[5]))
   print("UNIT_OF_MEASURE = " + (row[6]) + "\n")

print("Operation done successfully" + "\n")

conn.close()

print("Database closed successfully." + "\n")
