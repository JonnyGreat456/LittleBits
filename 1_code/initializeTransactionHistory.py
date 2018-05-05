# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import math 
import sqlite3 as sql 

app = Flask(__name__)

conn = sql.connect('transactionHistory.db')

print("Database opened successfully...")

conn.execute('''DROP TABLE IF EXISTS transactions;''')

conn.execute('''CREATE TABLE transactions (
    ID INTEGER NOT NULL,
    DETAILS TEXT NOT NULL,
    TRANSACTION_DATE TEXT NOT NULL,
    COST FLOAT NOT NULL
);''')

print("Table created successfully..." + "\n")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (0,'Initial Inventory Purchase','26MAR18', -19778.80);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (1,'Payroll Week', '26MAR18', -18424);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (2,'Daily Sales', '26MAR18', 7397.45);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (3,'Daily Sales', '27MAR18', 7263.09);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (4,'Daily Sales', '28MAR18', 4098.45);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (5,'Daily Sales', '29MAR18', 8397.5);")
      
conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (6,'Daily Sales', '30MAR18', 10001);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (7,'Daily Sales', '31MAR18', 5987.22);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (8,'Daily Sales', '01APR18', 8291.89);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (9,'Payroll Week', '02APR18', -18424);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (10,'Daily Sales', '02APR18', 6546.98);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (11,'Marinara Sauce Replacement', '02APR18', -192);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (12,'Daily Sales', '03APR18', 8127.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (13,'Spinach Dip Replacement', '03APR18', -24.95);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (14,'Frozen Cheese Pizza Replacement', '03APR18', -441.50);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (15,'Daily Sales', '04APR18', 6787.90);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (16,'Tomato Replacement', '04APR18', -90);")
      
conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (17,'Daily Sales', '05APR18', 7650);")
      
conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (18,'Daily Sales', '06APR18', 5632.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (19,'Daily Sales', '07APR18', 6789.96);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (20,'Daily Sales', '08APR18', 3490.87);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (21,'Cucumber Replacement', '08APR18', -72);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (22,'Payroll Week', '09APR18', -18424);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (23,'Daily Sales', '09APR18', 8027);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (24,'Daily Sales', '10APR18', 6827.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (25,'Daily Sales', '11APR18', 3459.90);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (26,'Daily Sales', '12APR18', 7856.43);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (27,'Daily Sales', '13APR18', 8887.90);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (28,'Celery Replacement', '13APR18', -149);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (29,'Daily Sales', '14APR18', 4367.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (30,'Daily Sales', '15APR18',2621.91);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (31,'Payroll Week', '16APR18', -18424);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (32,'Daily Sales', '16APR18', 9845.64);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (33,'Daily Sales', '17APR18', 3459.60);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (34,'Daily Sales', '18APR18', 7127.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (35,'Daily Sales', '19APR18', 4389.67);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (36,'Daily Sales', '20APR18', 3767.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (37,'Daily Sales', '21APR18', 9982.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (38,'Daily Sales', '22APR18', 4398.72);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (39,'Payroll Week', '23APR18', -18424);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (40,'Daily Sales', '23APR18', 6597.98);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (41,'Daily Sales', '24APR18', 4598.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (43,'Daily Sales', '25APR18', 5437.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (44,'Daily Sales', '26APR18', 3487.10);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (45,'Daily Sales', '27APR18', 5732.65);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (46,'Daily Sales', '28APR18', 3424.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (47,'Daily Sales', '29APR18', 4357.40);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (48,'Payroll Week', '30APR18', -18424);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (49,'Daily Sales', '30APR18', 8667.70);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (50,'Daily Sales', '01MAY18', 3928.46);")

conn.execute("INSERT INTO transactions (ID, DETAILS, TRANSACTION_DATE, COST) \
      VALUES (51,'Daily Sales', '02MAY18', 5392.90);")

print("Elements inserted successfully..." + "\n")

conn.commit()
cursor = conn.execute("SELECT ID, DETAILS, TRANSACTION_DATE, COST FROM transactions;")
for row in cursor:
   print("ID = " + str(row[0]))
   print("DETAILS = " + row[1])
   print("TRANSACTION_DATE = " + row[2])
   print("COST = " + str(row[3]) + "\n")

print("Operation done successfully" + "\n")

conn.close()

print("Database closed successfully." + "\n")
