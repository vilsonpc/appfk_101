#!/usr/bin/python3
# -*- coding: utf-8 -*-
# microframework Flask
from flask import Flask, render_template

# app object class
app = Flask(__name__)

# global variables

# function index
@app.route('/')
def index():
        # returns a simple template
        return render_template("index.html")

# if main
if __name__ == "__main__":
    # run server app 
    app.run(host ='0.0.0.0', port = 5000, debug = True)
    