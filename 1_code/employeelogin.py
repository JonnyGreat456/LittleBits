# -*- coding: utf-8 -*-
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/employeelogin/")
def employeelogin():
	return render_template("employeelogin.html")
	

app.run(debug = True)