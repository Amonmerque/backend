from flask import request, make_response, session
from flask_restful import Resource

from api import app, db, api, bcrypt
from flask import render_template

# from api.models import User, Movie, CartItem, Review
from api.models import Movie

# Views go here!
@app.route("/")
@app.route("/<int:id>")
def index(id=0):
 return render_template("index.html")

class AllMovies(Resource):
 def get(self):
#   movies = Movie.query.all()
# #   body = [movie.to_dict(rules=("-reviews.movie","-reviews.user","-cart_items.movie_cart","-cart_items.user_cart",)) for movie in movies]
#   body =""
#   return make_response(body, 200)
    # return 200
    movies = Movie.query.all()
    body = [movie.to_dict() for movie in movies]
    return make_response(body, 200)

 def post(self):
  try:
   new_movie = Movie(
    name=request.json.get("name"),
    image=request.json.get("image"),
    year=request.json.get("year"),
    director=request.json.get("director"),
    description=request.json.get("description"),
    price=request.json.get("price"),
   )
   db.session.add(new_movie)
   db.session.commit()
   body = new_movie.to_dict(
    rules=(
     "-reviews.movie",
     "-reviews.user",
     "-cart_items.movie_cart",
     "-cart_items.user_cart",
    )
   )
   return make_response(body, 201)
  except:
   body = {"error": "New movie could not be created."}
   return make_response(body, 400)
  
def test():
  new_movie = Movie(
  name="CACA",
  image="None",
  year=1985,
  director="ME",
  description="BOSS",
  price=1.0,
  )
  db.session.add(new_movie)
  db.session.commit()

api.add_resource(AllMovies, "/movies")