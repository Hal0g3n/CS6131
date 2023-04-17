from __main__ import app
import player, team, game, applications, tournament
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

@app.route("/player/leaderboard", methods=['GET'])
def getLeaderboard(): return player.leaderboard()



@app.route('/teams', methods=['GET'])
@jwt_required(optional=True)
def searchTeam():
    return team.search(**request.args)
    
@app.route('/teams/<team_id>', methods=['GET'])
@jwt_required(optional=True)
def getTeam(team_id): return team.getTeam(team_id)

@app.route('/teams/create', methods=['POST'])
@jwt_required()
def createTeam(): return team.createTeam(request.form['team_name'])

@app.route('/teams/quitMod', methods=['POST'])
@jwt_required()
def quitTeamMod(): return team.quitMod()

@app.route('/teams/quitTeam', methods=['POST'])
@jwt_required()
def quitTeam(): return team.quitTeam()



@app.route('/apply/team/<team_id>', methods=['GET', 'POST'])
@jwt_required()
def getApplyByTeam(team_id):
    if request.method == 'POST': return applications.create_application(team_id)
    if request.method == 'GET': return applications.get_applications(team_id = team_id)

@app.route('/apply/user/<username>', methods=['GET'])
@jwt_required()
def getApplyByUser(username): return applications.get_applications(username = username)

@app.route('/apply/approve', methods=['POST'])
@jwt_required()
def approveApply(): return applications.approve_application(int(request.form['team_id']), request.form['applicant'])

@app.route('/apply/delete', methods=['POST'])
@jwt_required()
def deleteApply(): return applications.delete_application(int(request.form['id']), int(request.form['team_id']), request.form['applicant'])



@app.route('/games/<id>', methods=['GET'])
@jwt_required(optional=True)
def getGame(id): return game.search(id = id)



@app.route('/tournament/<id>', methods=['GET', 'POST'])
@jwt_required(optional=True)
def getTournament(id): 
    if request.method == 'POST': return tournament.join(id)
    if request.method == 'GET':  return tournament.get(id = id)

@app.route('/tournament', methods=['GET'])
def searchTournaments(): return tournament.search()

@app.route('/tournament/create', methods=['POST'])
def createTournament(): return tournament.create()