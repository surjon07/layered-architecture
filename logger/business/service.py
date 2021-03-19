from flask import jsonify, request
from business import app
from data.repo import Repository

@app.route("/logs", methods=['POST', 'GET'])
def logs():
    response = Repository.logs()
    return jsonify([data.__str__() for data in response])

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        return Repository.login(email)

    return { 'success': False }

@app.route("/logout", methods=['POST', 'GET'])
def logout():
    if request.method == 'POST':
        email = request.form['email']
        return Repository.logout(email)

    return { 'success': False }

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name    = request.form['name']
        email   = request.form['email']
        return Repository.register(name, email)
        
    return { 'success': False }

@app.route("/employees", methods=['POST', 'GET'])
def employees():
    response = Repository.employees()
    return jsonify([data.__str__() for data in response])
