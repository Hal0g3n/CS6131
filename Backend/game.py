from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import get_jwt_identity
from flask import jsonify, request

import MySQLdb, re

from flask_app import mysql

def getGame(id = None): 
    # Check if player exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Games WHERE game_id = %s', (id,))
    game = cursor.fetchone()

    # LOL no such game
    if not game: return "No such ID", 403

    game['is_public'] = bool(game['is_public'])
    game['is_rated'] = bool(game['is_rated'])

    # Check if player can access the game
    if (game['is_public']): return game

    player = get_jwt_identity()
    if player and game['white_player'] == player: return game
    if player and game['black_player'] == player: return game

    # Player should not see the game
    return "No such ID", 403


def search(username):
    query = """
    SELECT p2.username opponent, IF(p1.username = white_name, 'white', 'black') side, is_public, 
    CASE
        WHEN pgn LIKE '%%0' THEN IF(p1.username = white_name, 1, -1)
        WHEN pgn LIKE '%%1' THEN IF(p1.username = white_name, -1, 1)
        ELSE 0
    END AS 'result', 
    datetime date
    FROM Players p1, Players p2, Games 
    WHERE 
        ((p1.username = white_name AND p2.username = black_name) OR 
        (p2.username = white_name AND p1.username = black_name)) AND
        p1.username = %s"""
        
    params = [username]
    if username != get_jwt_identity(): 
        query += " AND (is_public OR p2.username = %s)"
        params.append(get_jwt_identity() if get_jwt_identity() else '')

    # Check if player exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(query, tuple(params))
    
    return jsonify(list(map(lambda x: {**x, 'is_public': x['is_public'] == b'\x01'}, cursor.fetchall())))
