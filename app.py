import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")

@app.route("/index")
def index():
    recipes = mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/add_recipy")
def add_recipy():
    return render_template("add-recipy.html")


@app.route("/log_in")
def log_in():
    return render_template("log-in.html")


@app.route("/log_out")
def log_out():
    return render_template("log-out.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/week_menu_shuffle")
def week_menu_shuffle():
    return render_template("week-menu-shuffle.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

