import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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
    recipes = [
        recipe for recipe in mongo.db.recipes.aggregate(
            [{"$sample": {"size": 3}}])]
    return render_template("index.html", recipes=recipes)


@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template(
        "recipes.html", page_title="Recipes", recipes=recipes)


@app.route("/recipes/<recipe_name>")
def recipe_page(recipe_name):
    this_recipe = {}
    recipes = mongo.db.recipes.find()
    for recipe in recipes:
        if recipe["url"] == recipe_name:
            this_recipe = recipe
    return render_template("recipe.html", recipe=this_recipe,)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "time": request.form.get("time"),
            "country": request.form.get("country"),
            "ingredients": request.form.getlist("ingredients"),
            "description": request.form.get("description"),
            "image_url": request.form.get("url"),
            "url": request.form.get(
                "recipe_name").lower().replace(" ", "-"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("recipe added")
        return redirect(url_for('recipes', _external=True, _scheme='https'))
    return render_template("add-recipe.html", page_title="Add Recipe")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        edited_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "time": request.form.get("time"),
            "country": request.form.get("country"),
            "ingredients": request.form.getlist("ingredients"),
            "description": request.form.get("description"),
            "image_url": request.form.get("url"),
            "url": request.form.get(
                "recipe_name").lower().replace(" ", "-"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edited_recipe)
        flash("recipe succesfully edited")
        return redirect(url_for('recipes', _external=True, _scheme='https'))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "edit-recipe.html", page_title="Edit Recipe", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("recipe deleted")
    return redirect(url_for('recipes', _external=True, _scheme='https'))


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("new_username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for(
                "sign_in", _external=True, _scheme='https'))

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
        return redirect(url_for(
            'profile', username=session["user"],
            _external=True, _scheme='https'))

    return render_template("sign-up.html", page_title="Sign Up")


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
                return redirect(url_for(
                    'profile', username=session["user"],
                    _external=True, _scheme='https'))
            else:
                flash("Username and/or password incorrect")
                return redirect(url_for(
                    'log_in', _external=True, _scheme='https'))
        else:
            flash("Username and/or password incorrect")
            return redirect(url_for('log_in', _external=True, _scheme='https'))
    return render_template(
        "log-in.html", page_title="Log In")


@app.route("/log_out")
def log_out():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in", _external=True, _scheme='https'))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    user_recipes = mongo.db.recipes.find({"created_by": session["user"]})
    return render_template(
        "profile.html", user=user, user_recipes=user_recipes)


@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if request.method == "POST":
        edited_profile = {
            "$set":
                {"name": request.form.get("name"),
                    "email": request.form.get("email")}
        }
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, edited_profile)
        flash("Profile succesfully edited")
        return redirect(url_for(
            'profile', username=session["user"],
            _external=True, _scheme='https'))
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    print(user)
    return render_template(
        "edit-profile.html", page_title="Edit Profile", user=user)


@app.route("/edit_password/<user_id>", methods=["GET", "POST"])
def edit_password(user_id):
    if request.method == "POST":
        edited_password = {
            "$set":
                {"password": generate_password_hash(
                    request.form.get("new_password"))}
        }
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, edited_password)
        flash("Password succesfully edited")
        return redirect(url_for('profile', username=session["user"]))
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template(
        "edit-password.html", page_title="Edit Password", user=user)


@app.route("/delete_profile/<user_id>")
def delete_profile(user_id):
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User deleted")
    session.pop("user")
    return redirect(url_for('sign_up', _external=True, _scheme='https'))


@app.route("/week_menu_shuffle", methods=["GET", "POST"])
def week_menu_shuffle():
    if request.method == "POST":
        country = {"country": request.form.get("country")}
        return redirect(url_for('week_menu', country=country))
    return render_template(
        "week-menu-shuffle.html",
        page_title="Week Menu Shuffle")


@app.route("/week_menu/<country>")
def week_menu(country):
    print(country)
    recipes = mongo.db.recipes.find({"country": country})
    print(list(recipes))
    return render_template("week-menu.html", recipes=recipes, country=country,
                           page_title="Your Week Menu")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
