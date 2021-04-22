import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
    recipes = mongo.db.recipes.find()
    return render_template(
        "recipes.html", page_title="Recipes", recipes=recipes)


@app.route("/recipes/<recipy_name>")
def recipy_page(recipy_name):
    this_recipy = {}
    recipes = mongo.db.recipes.find()
    for recipy in recipes:
        if recipy["url"] == recipy_name:
            this_recipy = recipy
    return render_template("recipy.html", recipy=this_recipy)


@app.route("/api/recipes")
def api_recipes():
    recipes = mongo.db.recipes.find()
    print(recipes)
    return jsonify(recipes=recipes)


@app.route("/add_recipy")
def add_recipy():
    return render_template("add-recipy.html", page_title="Add Recipy")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    return render_template(
        "log-in.html", page_title="Log In")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for('log_in'))
        register = {
            "username": request.form.get("username").lower(),
            "name": request.form.get("name").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Succesful!")
    return render_template(
        "sign-up.html", page_title="Sign Up")


@app.route("/log_out")
def log_out():
    return render_template("log-out.html", page_title="Log Out")


@app.route("/profile")
def profile():
    return render_template("profile.html", page_title="Log Out")


@app.route("/week_menu_shuffle")
def week_menu_shuffle():
    return render_template(
        "week-menu-shuffle.html", page_title="Week Menu Shuffle")


@app.route("/recipy")
def recipy():
    return render_template("recipy.html", page_title="recipy")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

