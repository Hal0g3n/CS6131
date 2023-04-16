from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import jsonify, request

import MySQLdb, re
import base64

from flask_app import mysql

def create_application(team_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Check if user already in a team
    cursor.execute("SELECT * FROM Players WHERE username = %s",(get_jwt_identity(),))
    if cursor.fetchone()['team_id']: return "Already in team :/"


    # Make sure to delete previous occurrences of the application
    cursor.execute("DELETE FROM Applications where creator_name = %s AND team_id = %s", (get_jwt_identity(), team_id))
    mysql.connection.commit()

    cursor.execute("SELECT MAX(id) FROM Applications where creator_name = %s", (get_jwt_identity(), ))
    prev_id = cursor.fetchone()['MAX(id)']
    n_id = 1 + prev_id if prev_id else 0

    cursor.execute("INSERT INTO Applications(id, creator_name, team_id, message) VALUES (%s, %s, %s, %s)",(
        n_id,
        get_jwt_identity(),
        team_id,
        request.form['message']
    ))

    mysql.connection.commit() #commit the insertion
    return "Success!"

def get_applications(team_id = None, username = None):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # If collecting team application data
    if team_id:
        # Make sure player is moderator of team
        cursor.execute("SELECT * FROM Players WHERE username = %s", (get_jwt_identity(),))
        player = cursor.fetchone()
        if str(player['team_id']) != team_id or not player['mod_start_date']: return "Not moderator of team"

        # Execute actual query and return
        cursor.execute("SELECT * FROM Applications WHERE team_id = %s", (team_id, ))
        return jsonify(cursor.fetchall())


    # Collecting personal application data
    


def delete_application(id, team_id = None, username = None):
    pass


def approve_application(team_id, applicant):
    pass