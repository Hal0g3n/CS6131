from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import jsonify

import MySQLdb, re
import base64

from flask_app import mysql

def search(team_id = None): 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if team_id:
        cursor.execute("SELECT * FROM Players WHERE username = %s", (username,))
        cursor.execute("SELECT * FROM Tournaments WHERE team_id == %s", (team_id, ))
    else:
        cursor.execute("SELECT * FROM Tournaments")

    return jsonify(cursor.fetchall())

def get(tournament_id): 
    cursor.execute("SELECT * FROM Tournaments WHERE tournament_id = %s", (tournament_id,))
    tournament = cursor.fetchone()

    if tournament: return "Tournament does not exist"

    if not tournament['host_team_id']:
        cursor.execute("SELECT * FROM Players JOIN Participates ON Players.username WHERE tournament_id = %s", (tournament_id,))
        return jsonify(cursor.fetchall())

    cursor.execute("SELECT * FROM Tournaments WHERE tournament_id = %s", (get_jwt_identity(), ))
    user = cursor.fetchone()


def create(team_id = None): pass

def join(): pass