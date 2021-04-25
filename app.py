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


@app.route("/add_recipy", methods=["GET", "POST"])
def add_recipy():
    if request.method == "POST":
        recipy = {
            "recipy_name": request.form.get("recipy_name"),
            "time": request.form.get("time"),
            "country": request.form.get("country"),
            "ingredients": request.form.getlist("ingredients"),
            "description": request.form.get("description"),
            "image_url": request.form.get("url"),
            "url": request.form.get(
                "recipy_name").lower().replace(" ", "-"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipy)
        flash("Recipy added")
        return redirect(url_for('recipes'))
    return render_template("add-recipy.html", page_title="Add Recipy")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}!".format(request.form.get("username")))
                return redirect(url_for('profile', username=session["user"]))
            else:
                flash("Username and/or password incorrect")
                return redirect(url_for('log_in'))
        else:
            flash("Username and/or password incorrect")
            return redirect(url_for('log_in'))
    return render_template(
        "log-in.html", page_title="Log In")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("new_username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("new_username").lower(),
            "name": request.form.get("name").lower(),
            "password": generate_password_hash(
                request.form.get("new_password")),
            "email": request.form.get("email").lower()

        }
        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("new_username").lower()
        flash("You are now signed up, welcome!")
        return redirect(url_for('profile', username=session["user"]))

    return render_template("sign-up.html")


@app.route("/log_out")
def log_out():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["name"]
    return render_template(
        "profile.html", page_title="Log Out", username=username)


@app.route("/week_menu_shuffle")
def week_menu_shuffle():
    return render_template(
        "week-menu-shuffle.html", page_title="Week Menu Shuffle")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

