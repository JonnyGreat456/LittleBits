# -*- coding: utf-8 -*-
from flask import Flask, render_template,request
import math

import numpy as np

app = Flask(__name__)
chef_shifts = np.matrix([["","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],["James Beard","8:00am-10:00am","12:00pm-2:00pm","10:00am-12:00pm","2:00pm-4:00pm","4:00pm-6:00pm","6:00pm-8:00pm","8:00pm-10:00pm"],["Gordon Ramsay","2:00pm-4:00pm","8:00am-10:00am","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm"],["Jamie Oliver","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm"],["Emeril Lagasse","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm"],["Bobby Flay","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm"],["Rachael Ray","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm"],["Thomas Keller","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm","12:00pm-2:00pm"]])
busser_shifts = np.matrix([[" ","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],["8:00am-10:00am","","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["10:00am-12:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["12:00pm-2:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["2:00pm-4:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["4:00pm-6:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["6:00pm-8:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["8:00pm-10:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"]])
waiter_shifts = np.matrix([[" ","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],["8:00am-10:00am","James waiter","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["10:00am-12:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["12:00pm-2:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["2:00pm-4:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["4:00pm-6:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["6:00pm-8:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"],["8:00pm-10:00pm","James Beard","James Beard","Gordon Ramsay","Gordon Ramsay","Jamie Oliver","Jamie Oliver","Emeril Lagasse"]])


#we are creating three different matrices to view the shifts
#one matrix called chef_shifts will be to view the shifts for the chef
#another matrix called busser_shifts will be to view the shifts for the busser
#the third matrix called waiter_shifts will be to view the shifts for the waiter

#we need to create a text file so that the previous employee records can be saved and can be accessed any time


##since only the manager should be allowed to modify shifts, the manager will be given the write and append acess while the employee
##can access the text file only in read mode

@app.route("/")
def shifts():
	f= open("employeeshifts.txt","w+")

	for i in range(10):
		f.write("This is line %d\r\n" % (i+1))
	 
	f.close()

	with open('shiftsfile.txt','w') as ff:
		for line in chef_shifts:
			np.savetxt(ff, line, fmt='%s')
		for line in busser_shifts:
			np.savetxt(ff, line, fmt='%s')
		for line in waiter_shifts:
			np.savetxt(ff, line, fmt='%s')
		
	return render_template("viewshifts.html",result=chef_shifts)
	
@app.route('/upload/',methods = ['POST'])
def uploaduj():
	global chef_shifts
	global waiter_shifts
	global waiter_shifts
	chef_name = request.form['chefname']
	print("************************")
	print(str(chef_name))
	day_of_the_week = request.form['dayoftheweek']
	print(day_of_the_week)
	new_shift_timings = request.form['newshifttimings']
	print(new_shift_timings)
	index = request.form['jj']
	print(index)
	
	return (''), 204
	
if __name__ =="__main__":
	app.run(debug = True)
