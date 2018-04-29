# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import math 
import sqlite3 as sql 

app = Flask(__name__)

conn = sql.connect('menu.db')

print("Database opened successfully...")

conn.execute('''DROP TABLE IF EXISTS Menu;''')

conn.execute('''CREATE TABLE menu (
    ID INTEGER NOT NULL,
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
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (1,'Dessert', 'Lava Cake', 4.75, '4.3,3.4,4.4', 'Frozen Lava Cake', 0.53, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (2,'Dessert', 'Vanilla Ice Cream', 3.50, '3.7,4.0', 'Vanilla Ice Cream', 0.65, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (3,'Dessert', 'Chocolate Ice Cream', 3.50, '3.6,3.8', 'Chocolate Ice Cream', 0.65, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (4,'Dessert', 'Apple Pie', 4.25, '4.3,4.2', 'Frozen Apple Pie', 0.45, 'lbs');")

# Appetizer
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (5, 'Appetizer', 'Spinach Dip', 3.25, '3.2,3.6,2.9', 'Spinach Dip', 0.5, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (6, 'Appetizer', 'Stuffed Potatoe Skins', 5.00, '3.8,3.8', 'Potatoes', 2.00, 'lbs');")

conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (7, 'Appetizer', 'Buffalo Wings', 6.75, '4.1,3.4,3.7', 'Frozen Chicken Wings', 0.5, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (7, 'Appetizer', 'Buffalo Wings', 6.75, '4.1,3.4,3.7', 'Celery', 0.33, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (7, 'Appetizer', 'Buffalo Wings', 6.75, '4.1,3.4,3.7', 'Frying Oil', 0.1, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (7, 'Appetizer', 'Buffalo Wings', 6.75, '4.1,3.4,3.7', 'Ranch Dressing', 0.02, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (7, 'Appetizer', 'Buffalo Wings', 6.75, '4.1,3.4,3.7', 'Blue Cheese', 0.02, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (7, 'Appetizer', 'Buffalo Wings', 6.75, '4.1,3.4,3.7', 'Buffalo Sauce', 0.02, 'gal');")

conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (8, 'Appetizer', 'Barbeque Wings', 6.75, '4.1,3.4,3.7', 'Frozen Chicken Wings', 0.5, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (8, 'Appetizer', 'Barbeque Wings', 6.75, '4.1,3.4,3.7', 'Celery', 0.33, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (8, 'Appetizer', 'Barbeque Wings', 6.75, '4.1,3.4,3.7', 'Frying Oil', 0.1, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (8, 'Appetizer', 'Barbeque Wings', 6.75, '4.1,3.4,3.7', 'Ranch Dressing', 0.02, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (8, 'Appetizer', 'Barbeque Wings', 6.75, '4.1,3.4,3.7', 'Blue Cheese', 0.02, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (8, 'Appetizer', 'Barbeque Wings', 6.75, '4.1,3.4,3.7', 'Barbeque Sauce', 0.02, 'gal');")

conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (9, 'Appetizer', 'Mozzarella Sticks', 4.50, '4.8,4.3,4.2,4.9', 'Frozen Mozzarella Sticks', 0.5, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (9, 'Appetizer', 'Mozzarella Sticks', 4.50, '4.8,4.3,4.2,4.9', 'Frying Oil', 0.07, 'gal');")

# Kid's Menu
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (10, 'Kids Menu', 'Chicken Nuggets', 5.25, '5.0,4.9,5.0', 'Frozen Chicken Nuggets', 0.78, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (10, 'Kids Menu', 'Chicken Nuggets', 5.25, '5.0,4.9,5.0', 'Frying Oil', 0.07, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (10, 'Kids Menu', 'Chicken Nuggets', 2.50, '3.8,3.9,4.1', 'Frozen French Fries', 0.3, 'lbs');")

conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (11, 'Kids Menu', 'Cheese Pizza', 5.00, '3.0,4.0,5.0', 'Frozen Cheese Pizza', 1.25, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (11, 'Kids Menu', 'Cheese Pizza', 5.00, '3.0,4.0,5.0', 'Marinara Sauce', 0.3, 'lbs');")

conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (12, 'Kids Menu', 'Pepperoni Pizza', 5.25, '3.4,3.5,3.2', 'Frozen Cheese Pizza', 1.25, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (12, 'Kids Menu', 'Pepperoni Pizza', 5.25, '3.4,3.5,3.2', 'Pepperoni', 0.8, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (12, 'Kids Menu', 'Pepperoni Pizza', 5.25, '3.4,3.5,3.2', 'Marinara Sauce', 0.3, 'lbs');")

# Drinks
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (13, 'Drinks', 'Tea', 2.55, '3.4', 'Tea Bags', 0.007, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (14, 'Drinks', 'Coca Cola', 2.25, '3.7,2.5', 'Coca Cola Syrup', 0.05, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (15, 'Drinks', 'Sprite', 2.25, '3.8,4.1', 'Sprite Syrup', 0.05, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (16, 'Drinks', 'Coffee', 2.55, '3.8,2.9,4.6,4.1', 'Coffee Beans', 0.057, 'lbs');")

# Pasta 
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (17, 'Pasta', 'Lasagne', 12.25, '3.7,3.8,3.7', 'Frozen Lasagne', 0.58, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (17, 'Pasta', 'Lasagne', 12.25, '3.7,3.8,3.7', 'Marinara Sauce', 0.95, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (17, 'Pasta', 'Lasagne', 12.25, '3.7,3.8,3.7', 'Mozzarella Cheese', 0.5, 'lbs');")

conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (18, 'Pasta', 'Macaroni and Cheese', 10.50, '4.3,4.1', 'Macaroni Shells', 1.00, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (18, 'Pasta', 'Macaroni and Cheese', 10.50, '4.3,4.1', 'Mozzarella Cheese', 0.5, 'lbs');")

conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (19, 'Pasta', 'Ravioli', 11.75, '3.2,2.9,3.8', 'Frozen Ravioli', 1.15, 'lbs');")

conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (20, 'Pasta', 'Chicken Alfredo Pasta', 13.25, '3.4,3.2', 'Canned Alfredo Sauce', 0.33, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (20, 'Pasta', 'Chicken Alfredo Pasta', 13.25, '3.4,3.2', 'Parmesan Cheese', 0.15, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (20, 'Pasta', 'Chicken Alfredo Pasta', 13.25, '3.4,3.2', 'Frozen Chicken Tenders', 0.15, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (20, 'Pasta', 'Chicken Alfredo Pasta', 13.25, '3.4,3.2', 'Penne Pasta Shells', 1.25, 'lbs');")

# Soup
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (21, 'Soup', 'Chili', 8.75, '3.3,3.0,4.0', 'Canned Chili without Beans', 0.75, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (22, 'Soup', 'Beef and Vegetable Soup', 8.95, '3.2,2.9,3.5', 'Beef Broth', 0.65, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (23, 'Soup', 'French Onion Soup', 8.50, '4.2,4.3,3.7', 'Yellow Onions', 0.52, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (23, 'Soup', 'French Onion Soup', 8.50, '4.2,4.3,3.7', 'Frozen White Bread Dough', 0.25, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (24, 'Soup', 'Tomato Soup', 8.25, '1.5,3.4,2.6,3.8,2.5', 'Canned Tomato Soup', 0.75, 'lbs');")

# Sides
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (25, 'Sides', 'House Salad', 3.00, '3.2,4.1,3.7', 'Italian Dressing', 0.045, 'gal');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (25, 'Sides', 'House Salad', 3.00, '3.2,4.1,3.7', 'Tomatoes', 0.25, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (25, 'Sides', 'House Salad', 3.00, '3.2,4.1,3.7', 'Cucumber', 0.25, 'lbs');")
conn.execute("INSERT INTO Menu (ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure) \
      VALUES (25, 'Sides', 'House Salad', 3.00, '3.2,4.1,3.7', 'Croutons', 0.2, 'lbs');")


print("Elements inserted successfully..." + "\n")

conn.commit()
cursor = conn.execute("SELECT ID, category, itemName, itemPrice, listRatings, ingredientName, quantity, unitOfMeasure from menu;")
for row in cursor:
   print("ID = " + (row[0]))
   print("CATEGORY = " + (row[1]))
   print("ITEM_NAME = " + (row[2]))
   print("ITEM_PRICE = " + str(row[3]))
   print("LIST_OF_RATINGS = " + (row[4]))
   print("INGREDIENT_NAME = " + (row[5]))
   print("QUANTITY = " + str(row[6]))
   print("UNIT_OF_MEASURE = " + (row[7]) + "\n")

print("Operation done successfully" + "\n")

conn.close()

print("Database closed successfully." + "\n")
