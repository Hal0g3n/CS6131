from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import jsonify, request

import MySQLdb, re
import base64

from flask_app import mysql


def search():
    """
    Get all teams with search params using MySQL
    """
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if 'name' in request.args: cursor.execute('SELECT * FROM Teams WHERE team_name LIKE %s', ("%{}%".format(request.args['name']),))
    else: cursor.execute("SELECT * FROM Teams")
    
    # Return all teams
    return jsonify(list(map(
        lambda team: {**team, 'icon': "data:image/png;base64," + base64.b64encode(team['icon']).decode()},
        cursor.fetchall()
    )))