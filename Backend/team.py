from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import jsonify

import MySQLdb, re
import base64

from flask_app import mysql


def search(name = None, team_id = None):
    """
    Get all teams with search params using MySQL
    """
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    query = "SELECT * FROM Teams WHERE true"
    params = []

    if name: 
        query += " AND team_name LIKE %%s%"
        params.append(request.args['name'])

    if team_id: 
        query += " AND team_id = %s"
        params.append(int(team_id))

    cursor.execute(query + " ORDER BY member_count DESC", tuple(params))
    
    # Return all teams
    return jsonify(list(map(
        lambda team: {**team, 'icon': "data:image/png;base64," + base64.b64encode(team['icon']).decode() if team['icon'] else None},
        cursor.fetchall()
    )))

def getTeam(id):
    """
    Get the team information and all players in the team
    """
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Get the team info with the given id
    cursor.execute("SELECT * FROM Teams WHERE team_id = %s", (id, ))
    team = cursor.fetchone()

    # Query all players and their respective ratings
    cursor.execute("""
    SELECT username, avatar, (
        SELECT rating 
        FROM Rating_History hist 
        WHERE hist.username = Players.username 
        ORDER BY datetime
        DESC LIMIT 1
    ) rating, (
        SELECT rating 
        FROM Puzzle_History hist 
        WHERE hist.username = Players.username 
        ORDER BY datetime
        DESC LIMIT 1
    ) puzzle,
    IF (mod_start_date IS NULL, 0, 1) is_moderator
    FROM Players
    WHERE team_id = %s
    """, (id, ))

    team['players'] = list(map(
        lambda player: {**player, 'avatar': "data:image/png;base64," + base64.b64encode(player['avatar']).decode() if player['avatar'] else None}, 
        cursor.fetchall() 
    ))

    team['icon'] = "data:image/png;base64," + base64.b64encode(team['icon']).decode() if team['icon'] else None

    return jsonify(team)


def createTeam(team_name):
    # Check if team exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Teams WHERE team_name = %s', (team_name,))
    team = cursor.fetchone()

    if team: return "Team already exists", 403

    # Username check
    if not re.match(r'^[A-Za-z0-9 ]+$', team_name): return "Invalid Team Name", 403

    # Team does not exists and the form data is valid, now insert new team into teams table
    cursor.execute('INSERT INTO Teams(team_name, creation_date) VALUES (%s, NOW())', (team_name,))
    mysql.connection.commit() #commit the insertion

    # Get the team object
    cursor.execute('SELECT * FROM Teams WHERE team_name = %s', (team_name,))
    team = cursor.fetchone()

    cursor.execute('''
    UPDATE Players SET team_id = %s, join_date = NOW(), mod_start_date = NOW()
    WHERE username = %s
    ''', (team['team_id'], get_jwt_identity(),))
    mysql.connection.commit() #commit the update

    team['icon'] = "data:image/png;base64," + base64.b64encode(team['icon']).decode() if team['icon'] else None
    return jsonify(team)

def quitMod():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''
    UPDATE Players SET mod_start_date = NULL
    WHERE username = %s
    ''', (get_jwt_identity(),))
    mysql.connection.commit() #commit the update
    
    return "Success!"

def promoMod(username, team_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Make sure initiator is moderator of team
    cursor.execute("SELECT * FROM Players WHERE username = %s", (get_jwt_identity(),))
    player = cursor.fetchone()
    print(1)
    if str(player['team_id']) != team_id or not player['mod_start_date']: return "Not moderator of team", 403
    print(2)

    # Make sure player is part of team
    cursor.execute("SELECT * FROM Players WHERE username = %s", (username,))
    player = cursor.fetchone()
    if str(player['team_id']) != team_id: return "User cannot be moderator", 403

    # Now update promote the player
    cursor.execute('''
    UPDATE Players SET mod_start_date = NOW()
    WHERE username = %s
    ''', (username,))
    mysql.connection.commit() #commit the update

    return "Success!"


def quitTeam():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''
    UPDATE Players SET mod_start_date = NULL, team_id = NULL, join_date = NULL
    WHERE username = %s
    ''', (get_jwt_identity(),))
    mysql.connection.commit() #commit the update
    
    return "Success!"

def kick(username, team_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Make sure initiator is moderator of team
    cursor.execute("SELECT * FROM Players WHERE username = %s", (get_jwt_identity(),))
    player = cursor.fetchone()
    
    if str(player['team_id']) != team_id or not player['mod_start_date']: return "Not moderator of team", 403

    # Make sure player is part of team
    cursor.execute("SELECT * FROM Players WHERE username = %s", (username,))
    player = cursor.fetchone()
    if str(player['team_id']) != team_id: return "User not in team", 403

    # Kick the poor player
    cursor.execute('''
    UPDATE Players SET mod_start_date = NULL, team_id = NULL, join_date = NULL
    WHERE username = %s
    ''', (username,))
    mysql.connection.commit() #commit the update
    return "Success!"