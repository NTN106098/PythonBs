from flask import Flask
from flask_pymongo import PyMongo




app = Flask(__name__)



from app import views
from app import admin_views
