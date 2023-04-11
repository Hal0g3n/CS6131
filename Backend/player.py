from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt
from flask import jsonify, request

import MySQLdb, re, pickle

from flask_app import mysql, blacklist, BLACKLIST_FILE

def login():
    """
    Login Player (returning jwt token)
    """
    if 'username' not in request.form or 'password' not in request.form:
        return "Malformed Request", 400

    # Create variables for easy access
    username = request.form['username']
    password = request.form['password']

    # Check if player exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Players WHERE username = %s', (username,))
    player = cursor.fetchone()

    if player and check_password_hash(player['password'], password):
        access_token = create_access_token(identity=player['username'])
        return jsonify(access_token = access_token)
    else:
        return jsonify(message = "Incorrect Username/Password")
    

def register():
    """
    Registers new Player (Does not give jwt token)
    Player must then login
    """   
    if 'username' not in request.form or 'password' not in request.form:
        return "Malformed Request", 400

    # Create variables for easy access
    username = request.form['username']
    password = request.form['password']

    # Check if player exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Players WHERE username = %s', (username,))
    player = cursor.fetchone()

    if player: return "Account already exists", 403

    # Username check
    if not re.match(r'^[A-Za-z0-9]+$', username): return "No SQLI", 403

    print(generate_password_hash(password), len(generate_password_hash(password)))

    # Account does not exists and the form data is valid, now insert new player into accounts table
    cursor.execute('INSERT INTO Players(username, password) VALUES (%s, %s)', (username, generate_password_hash(password),))
    mysql.connection.commit() #commit the insertion

    return "Success", 200


def search(): pass

def update(): pass

def read(username):
    pass

def delete():
    pass