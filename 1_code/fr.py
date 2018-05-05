#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('employeeshiftsdb.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE EMPLOYEESHIFTS
         (NAME           TEXT    NOT NULL,
         ROLE            TEXT     NOT NULL,
		 DAY             TEXT     NOT NULL,
         SHIFTSTART      INT     NOT NULL,
         SHIFTEND        INT     NOT NULL,
		 STARTPERIOD	 TEXT     NOT NULL,
		 ENDPERIOD	 TEXT     NOT NULL);''')
print "Table created successfully";




conn.close()