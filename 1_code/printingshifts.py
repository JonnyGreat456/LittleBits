#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('employeeshiftsdb.db')
print "Opened database successfully";

cursor = conn.execute("SELECT NAME,ROLE,DAY,SHIFTSTART,SHIFTEND,STARTPERIOD,ENDPERIOD from EMPLOYEESHIFTS")
for row in cursor:
	print "NAME = ", row[0]
	print "ROLE = ", row[1]
	print "DAY = ", row[2]
	print "SHIFTSTART = ", row[3], "\t"
	print row[5], "\t"
	print "SHIFTEND = ", row[4], "\t"
	print row[6], "\t"
print "Operation done successfully";
conn.close()