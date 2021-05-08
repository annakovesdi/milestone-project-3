recipy site (software is) Eating the world 

To deploy the site, i started right at the beginning by installing flask and 



ref:
https://pymongo.readthedocs.io/en/stable/tutorial.html
https://jinja.palletsprojects.com/en/2.11.x/templates/#filters
https://materializecss.com/

defensive strategies

problems: 
did not show image. put url instead of image_url and it did not render correctly.
could not insert new user, wrong name tags in html

recipe url no special characters allowed, spaces replaced with -, lower

@app.route("/api/recipes")
def api_recipes():
    recipes = mongo.db.recipes.find()
    print(recipes)
    return jsonify(recipes=recipes)

replace recipy for recipe
tutor Tim
shuffle = [recipe for recipe in mongo.db.YourCollectionName.aggregate([{"$sample": {"size": 7}}])]    

https://stackoverflow.com/questions/10290621/how-do-i-partially-update-an-object-in-mongodb-so-the-new-object-will-overlay answer Eran Medan
How to update only some fields

to do: 
-week menu shuffle
-add 10 recp. per country
-value in stars option?
-list ingredients!
=cancel button @ add recipe, and edit profile, and edit password
-search function @ recipes page
-pop up before deleting recipy or profile
*-ingredients field big enough for text (textarea)
*-log out when deleting profile (bug) 
-delete all recipes of profile?
-backend defensive programming
=change url to slug


recipes = mongo.db.recipes.find({"country": country})
    shuffle = [
        recipe for recipe in recipes.aggregate(
            [{"$sample": {"size": 7}}])]

@app.route("/week_menu/<country>")
def week_menu(country):
    this_country = {}
    countries = mongo.db.recipes.find(
            {"country": request.form.get("country")})
    for item in countries:
        if item["country"] == country:
            this_country = item
    return render_template("week-menu.html", country=this_country,
                           page_title="Your {} Week Menu".format(
                               request.form.get("country")))
