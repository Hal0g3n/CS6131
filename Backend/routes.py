from flask_app import app
import player, team, game

from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

@app.route("/player/login", methods=["POST"])
def login(): return player.login()

@app.route('/player/new', methods=['POST'])
def register(): return player.register()

@app.route("/player/<username>", methods=["POST"])
@jwt_required(optional = True)
def readUser(username): return player.read(username)


@app.route('/teams', methods=['GET'])
@jwt_required(optional=True)
def searchTeam(): return team.search()
    
@app.route('/teams/<team_id>', methods=['GET'])
@jwt_required(optional=True)
def getTeam(id): return team.search(id = id)


@app.route("/auth", methods=['POST'])
@jwt_required()
def auth(): return "hello"


@app.route('/games/<id>', methods=['GET'])
@jwt_required(optional=True)
def getGame(id): return game.search(id = id)


@app.route('/create/team', methods=['POST'])
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
