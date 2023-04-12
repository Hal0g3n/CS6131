from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import get_jwt_identity
from flask import jsonify, request

import MySQLdb, re

from flask_app import mysql

def search(id = None): 
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