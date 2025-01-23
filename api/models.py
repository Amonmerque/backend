# models.py File
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from api import db

# Models go here!
class Movie(db.Model, SerializerMixin):
 __tablename__ = "movies"

 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String, unique=True)
 image = db.Column(db.String, nullable=False)
 year = db.Column(db.Integer, nullable=False)
 director = db.Column(db.String, nullable=False)
 description = db.Column(db.String, nullable=False)
 price = db.Column(db.Float, nullable=False)

 reviews = db.relationship("Review", back_populates="movie", cascade="all")
 cart_items = db.relationship("CartItem", back_populates="movie_cart", cascade="all")

 users = association_proxy("reviews", "user", creator=lambda u: Review(user=u))
 user_item = association_proxy(
"cart_items", "user_cart", creator=lambda ui: CartItem(user_cart=ui)
)

 @validates("name", "image", "director", "description")
 def validate_fields(self, key, value):
  if not value:
   raise ValueError(f"{key} must be completed.")
  else:
   return value

 @validates("year")
 def validate_year(self, key, value):
  if not (isinstance(value, int)) and (1900 <= value):
   raise ValueError("Year must be an integer and it has to be greater than 1900."
)
  else:
   return value