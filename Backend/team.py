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

    cursor.execute(query, tuple(params))
    
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