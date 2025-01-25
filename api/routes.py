from flask import request, make_response, session
from flask_restful import Resource
from flask_cors import CORS, cross_origin
from api import app, db, api, bcrypt
from flask import render_template

# from api.models import User, Movie, CartItem, Review
from api.models import Users
# from api.models import Movie, Users

# Views go here!
@app.route("/")
@cross_origin()
def index(id=0):
 return render_template("index.html")

@app.route("/users")
@cross_origin()
def getUsers():
  users = Users.query.all()
  body = [user.to_dict() for user in users]
  return make_response(body, 200)

@app.route("/user/create", methods=["POST"])
@cross_origin()
def user_create():
  if request.method == "POST":
    data=request.get_json()
    d_nom=data['nom']
    d_prenom=data['prenom']
    d_solde=data['solde']
    user = Users(nom=d_nom, prenom=d_prenom, solde=d_solde)
    db.session.add(user)
    db.session.commit()
    users = Users.query.all()
    body = [user.to_dict() for user in users]
    return make_response(body, 200)
  else:
    return make_response(dict(), 404)

@app.route("/user/beer", methods=["POST"])
@cross_origin()
def take_beer():
  if request.method == "POST":
    data=request.get_json()
    d_id=data['id']
    user = Users.query.filter_by(id=d_id).first()
    if user.solde >= 2:
      user.solde = user.solde-2
      db.session.commit()
      users = Users.query.all()
      body = [user.to_dict() for user in users]
      return make_response(body, 200)
    else:
      return {"error": "Invalid email"}, 400
    
@app.route("/user/delete", methods=["POST"])
@cross_origin()
def delete_user():
  if request.method == "POST":
    data=request.get_json()
    d_id=data['id']
    user = Users.query.filter_by(id=d_id).first()
    print(user.id)
    db.session.delete(user)
    db.session.commit()
    users = Users.query.all()
    body = [user.to_dict() for user in users]
    return make_response(body, 200)

  