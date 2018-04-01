# -*- coding: utf-8 -*-
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
	with open("customerplaceorder.html") as fp:
		soup = BeautifulSoup(fp)
	soup = BeautifulSoup("<html>data</html>")
	return render_template("customerplaceorder.html")

if __name__ == '__main__':
   app.run(debug = True)

   
   
   



