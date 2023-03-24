from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

# Here you can globally configure all the ways you want to allow JWTs to
# be sent to your web application. By default, this will be only headers.
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]

# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
app.config["JWT_COOKIE_SECURE"] = False

# Change this in your code!
app.config["JWT_SECRET_KEY"] = "super-secret"

jwt = JWTManager(app)


# Enter your database connection details below
app.config['MYSQL_HOST'] = 'db4free.net'
app.config['MYSQL_USER'] = 'halogen'
app.config['MYSQL_PASSWORD'] = 'Pearson1'
app.config['MYSQL_DB'] = 'chessible'

# Intialize MySQL
mysql = MySQL(app)


@app.route("/login", methods=["POST"])
def login():
    if 'username' not in request.form or 'password' not in request.form:
        return "Malformed Request", 400

    # Create variables for easy access
    username = request.form['username']
    password = request.form['password']
    
    # Check if account exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Player WHERE username = %s', (username,))
    account = cursor.fetchone()

    if account and check_password_hash(account['password'], password):
        access_token = create_access_token(identity=account['username'])
        return jsonify(access_token = access_token)
    else:
        return jsonify(message = "Incorrect Username/Password")


@app.route("/jwt-login", methods=["POST"])
def jwt_login():
    response = jsonify({"msg": "login successful"})
    access_token = create_access_token(identity="example_user")
    set_access_cookies(response, access_token)
    return response


@app.route('/logout', methods=['POST'])
@jwt_required
def logout():
    return 'Logout ' + current_identity, 200


@app.route('/register', methods=['POST'])
def register():
    if 'username' not in request.form or 'password' not in request.form:
        return "Malformed Request", 400

    # Create variables for easy access
    username = request.form['username']
    password = request.form['password']

    # Check if account exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Player WHERE username = %s', (username,))
    account = cursor.fetchone()

    if account: return "Account already exists", 403

    # Username check
    if not re.match(r'[A-Za-z0-9]+', username): return "No SQLI", 403
    
    # Account does not exists and the form data is valid, now insert new account into accounts table
    cursor.execute('INSERT INTO Player(username, password) VALUES (%s, %s)', (username, generate_password_hash(password),))
    mysql.connection.commit() #commit the insertion

    return "Success", 200

if __name__ == '__main__':
    app.run(debug=True)