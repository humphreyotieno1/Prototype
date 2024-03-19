#!/usr/bin/python3

from flask import Flask, render_template

app = Flask('templates')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
