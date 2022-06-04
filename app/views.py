from xml.sax import make_parser
from app import app
from flask import render_template, url_for
from flask_pymongo import PyMongo


app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)

@app.route("/")
def index():
    tours = mongo.db.Trip.find()
    return render_template('public/home/home.html', tours=tours)
    
@app.route("/about")
def about():
    return render_template('admin/login.html')
