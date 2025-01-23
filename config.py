import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

class Config:
#  SECRET_KEY = os.getenv("SECRET_KEY")
#  SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
#  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = "npg_0b5hXqkCUHtu"
  SQLALCHEMY_DATABASE_URI = "postgresql://neondb_owner:npg_0b5hXqkCUHtu@ep-old-mountain-a25cfcsg-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require"
  SQLALCHEMY_TRACK_MODIFICATIONS = False