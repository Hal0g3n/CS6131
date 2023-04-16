from __main__ import app
import player, team, game, applications
from flask import request
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

@app.route("/player/login", methods=["POST"])
def login(): return player.login()

@app.route('/player/new', methods=['POST'])
def register(): return player.register()

@app.route("/player/<username>", methods=["GET"])
@jwt_required(optional = True)
def readUser(username): return player.read(username)


@app.route('/teams', methods=['GET'])
@jwt_required(optional=True)
def searchTeam(): return team.search(**request.args)
    
@app.route('/teams/<team_id>', methods=['GET'])
@jwt_required(optional=True)
def getTeam(team_id): return team.getTeam(team_id)

@app.route('/teams/create', methods=['POST'])
def createTeam():
    if 'team_name' not in request.form:
        return "Malformed Request", 400

    # Create variables for easy access
    team_name = request.form['team_name']

    # Check if team exists using MySQL
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Teams WHERE team_name = %s', (team_name,))
    team = cursor.fetchone()

    if team: return "Team already exists", 403

    # Username check
    if not re.match(r'^[A-Za-z0-9 ]+$', team_name): return "No SQLI", 403

    # Team does not exists and the form data is valid, now insert new team into teams table
    cursor.execute('INSERT INTO Teams(team_name) VALUES (%s)', (Teams))
    mysql.connection.commit() #commit the insertion

    return "Success", 200


@app.route('/apply/team/<team_id>', methods=['GET', 'POST'])
@jwt_required()
def apply(team_id):
    if request.method == 'POST': return applications.create_application(team_id)
    if request.method == 'GET': return applications.get_applications(team_id = team_id)

@app.route('/apply/user/', methods=['GET'])
@jwt_required()
def apply(): return applications.get_applications()


@app.route("/auth", methods=['POST'])
@jwt_required()
def auth(): return "hello"


@app.route('/games/<id>', methods=['GET'])
@jwt_required(optional=True)
def getGame(id): return game.search(id = id)