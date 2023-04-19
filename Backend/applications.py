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
        if str(player['team_id']) != team_id or not player['mod_start_date']: return "Not moderator of team", 403

        # Execute actual query and return
        cursor.execute("SELECT * FROM Applications WHERE team_id = %s", (team_id, ))
        return jsonify(cursor.fetchall())

    # Collecting personal application data (with team name)
    cursor.execute("SELECT team_name, Applications.* FROM Applications NATURAL JOIN Teams WHERE creator_name = %s", (get_jwt_identity(), ))
    res = cursor.fetchall()
    return jsonify(res)


def delete_application(id, team_id = None, username = None):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if not username:
        # Delete user's own applications
        cursor.execute("DELETE FROM Applications where creator_name = %s AND team_id = %s AND id = %s", (get_jwt_identity(), team_id, id))
        mysql.connection.commit()

    else: # Delete team application
        # Make sure player is moderator of team
        cursor.execute("SELECT * FROM Players WHERE username = %s", (get_jwt_identity(),))
        player = cursor.fetchone()

        if player['team_id'] != team_id or not player['mod_start_date']: return "Not moderator of team", 403

        # Delete because you got rejected :/
        cursor.execute("DELETE FROM Applications where creator_name = %s AND team_id = %s AND id = %s", (username, team_id, id))
        mysql.connection.commit()

    return "Success!"


def approve_application(team_id, applicant):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Yay you got approved
    cursor.execute("UPDATE Applications SET approver_name = %s WHERE team_id = %s AND creator_name = %s", (get_jwt_identity(), team_id, applicant))
    mysql.connection.commit()

    # Delete all applications because applicant is accepted
    cursor.execute("DELETE FROM Applications where creator_name = %s", (applicant,))
    mysql.connection.commit()

    return "Success!"