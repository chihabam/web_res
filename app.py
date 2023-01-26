#!/bin/python
from flask import Flask, render_template, url_for
#from views import views

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('resume.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
