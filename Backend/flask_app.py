from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import re
import pickle
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

# JWT auth stuff
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt

# Here you can globally configure all the ways you want to allow JWTs to
# be sent to your web application. By default, this will be only headers.
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]

# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
app.config["JWT_COOKIE_SECURE"] = False

# Change this in your code!
app.config["JWT_SECRET_KEY"] = "Cheese Cake"

jwt = JWTManager(app)


# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'Chessible'

# Intialize MySQL
mysql = MySQL(app)


BLACKLIST_FILE = 'blacklist.pickle'

# Load the blacklist from file, if it exists
blacklist = set()

try:
    with open(BLACKLIST_FILE, 'rb') as f:
        blacklist = pickle.load(f)
except: pass

# Load the blacklist
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    print(blacklist)
    jti = jwt_payload['jti']
    return jti in blacklist

# Simple Logout Function
# Add token to blacklist
@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Revoke the current token by adding its jti to the blacklist
    jti = get_jwt()['jti']
    blacklist.add(jti)

    # Save the blacklist to file
    with open(BLACKLIST_FILE, 'wb') as f:
        pickle.dump(blacklist, f)

    return "Logout Successful"

import routes

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)