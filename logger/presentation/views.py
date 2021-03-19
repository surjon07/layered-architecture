from flask import Flask, render_template, request, redirect, url_for
from presentation import app
import requests

url = "http://127.0.0.1:5000"

@app.route("/")
def home():
    response = requests.get(url + "/logs")
    return render_template("index.html", data=response.json())

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = {
            'email'   : request.form['email']
        }
        requests.post(url = url + "/login", data = data)

    return redirect(url_for('home'))

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    if request.method == 'POST':
        data = {
            'email'   : request.form['email']
        }
        requests.post(url = url + "/logout", data = data)
    
    return redirect(url_for('home'))

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        data = {
            'name'    : request.form['name'],
            'email'   : request.form['email']
        }
        requests.post(url = url + "/register", data = data)
        return redirect(url_for('register'))

    response = requests.get(url + "/employees")
    return render_template("register.html", data=response.json())