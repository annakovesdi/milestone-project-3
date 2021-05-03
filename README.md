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
-log out when deleting profile (bug) 
-delete all recipes of profile?
-forgot password?

