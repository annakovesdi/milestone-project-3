# **Eating the World**

### Recipy site (software is) Eating the world

**A colourful recipe website that let's you create your own profile where you can add your own recipes,
has a search function to check out the recipes that are added by all users and has an extra special feature: a Week menu Shuffle!
This will shuffle a week menu for you, with all recipes of a country (so the ingredients and spices will probably align enough)
that you can enjoy a fully Italian (or any other country) themed week.**

## UX
The ideal visitor likes to cook, is interested in different kitchens from all over the world and would like to participate in creating a varied and interesting online scource of inspiration for other users.

Visitors are searching for recipes, that they can understand easily, find quickly and get them inspired to cook.
Ideally the visitor is equally interested to share their own recipes and thus contribute to the value of the site.

### _Visitor stories_
1. As a new visitor, I want to easily find my way to a recipe.
2. As a new visitor, I want to be able to search in the recipe for a dish, a country or an ingredient. 
3. As a new visitor, I want to sign up. 
4. As a returning visitor, I would like to log in.
5. As a user, i would like to see my profile and my added recipes.
6. As a user, i would like to edit my profile information and/or my password.
7. As a user, i would like to add a recipe.
8. As a user, i would like to edit or delete my recipe.
9. As a user, i would like to delete my profile and all my recipes. 
10. As a true enthausiast, i would like the site to create a country themed week menu for me.

Visitors find the experience they are searching for because:

This site is colourful and attractive. It is very easy to use and provides the millenial or z-generation hero with an answer to the 
most grinding question in adulting: 

>"How can I decide what to eat tonight, every night, for the rest of my life?"

With the week menu shuffle, in just one click, you solved a huge everyday problem and have energy left for other crucial stuff: like getting a mortgage. 

## Wireframes

![Index html mobile](/static/img/wireframes/index-html-mobile.png "index html mobile")



Features
The game features three overlays and the main page.

Overlay "seconds" is the first thing a player sees when visiting the site. This overlay is a black and white gif of a woman's knees, lifting up her skirt above them and placing the skirt back down as well. The title is How Naughty is your memory? And under that, you can select the number of seconds that you would like to complete the game. When you click on the play icon, the overlay closes.

Index.html page features a memory game of 30 cards, a countdown of the seconds that the player chose, and a counter of flips. The cards flip on click and display a drawing of a pin-up, they are paired - when the player finds two the same they stay 'open'. This lasts until all cards are flipped, on which the "victory" overlay is activated, or the countdown finishes, and the "lost" overlay is displayed.

"Victory" overlay displays a black and white gif of a sexy moving Dita von Teese and the text: Victory, enjoy your Teese. After 6 seconds the overlay changes automatically to the "seconds" overlay.

"Lost" overlay displays a black and white gif of a stern-looking woman, with the text: Oh no! You lost. After 6 seconds the overlay changes automatically to the "seconds" overlay.

Features to implement in the future:

The game could be improved by making the player choose the number of cards as well
Adding more games with the same theme to choose from
etc
Technologies used
Gitpod to develop the website
GitHub to deploy the website
Google fonts for the old fashioned font
Html, Css and JavaScript are the developing languages
moqups.com for the wireframes
lambdatest.com for static testing
Chrome dev tools for manual testing
Testing
Testing information can be found in the TESTING.md file

Deployment
The game is deployed through GitHub.

Steps to setup GitHub deployment:

Go to your project's Code & Deploys page, in the Repository tab.
Click the CONNECT TO GITHUB button to connect your project with GitHub.
Connect to one of your GitHub repositories.
Configure the deploy options.
Deploy your project. (as described by https://support.zyte.com/)
This is what I did. The configuration is on auto, which means that the repository will get updated if I push something from the connected GitPod dev area. The site is now live at https://annakovesdi.github.io/milestone-project-2/

You can clone a repository from GitHub to your local computer to make it easier to fix merge conflicts, add or remove files, and push larger commits. When you clone a repository, you copy the repository from GitHub to your local machine.

Cloning a repository pulls down a full copy of all the repository data that GitHub has at that point in time, including all versions of every file and folder for the project. You can push your changes to the remote repository on GitHub, or pull other people's changes from GitHub. How to do this is described dtep by step at https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

Credits
While starting to try to tackle Javascript I recreated two youtube tutorials in their entirety. These tutorials are:

Memory Card Game - JavaScript Tutorial (https://www.youtube.com/watch?v=ZniVgo8U7ek&t=4s) by FreeCodeCamp.org
and

How To Code A Card Game In Plain JavaScript - Spooky Halloween Edition (https://www.youtube.com/watch?v=3uuQ3g92oPQ&t=2637s) by PortEXE
I relied heavily on these resources to write my code. I am sure a lot of the logic of the tutorials is completely integrated into my project. I watched them so often, I can recite them in my sleep. It was very hard to get a hang of Javascript for me but I have to say that I really start to "get" it, finally, and am planning to practice A LOT.
Towards the end, the code was flowing, and I could solve issues by myself (i got the help of tutors before that). I tried to credit my code where appropiate. I hope you understand that it is not that clear: I try to refrain from copy pasting code in it's entirety. I change things as I go along. The credit is there, sometimes almost the same, sometimes more as the inspiring and teaching scource from where it started.

The memory card game tutorials were my beacon the darkness, my lighthouse in a stormy sea, my refuge from a desperate stackoverflow wormhole. I can not credit them enough for helping me forward and making this game.

To get a hang of the subject I did:

The entire Javascript coding chapter of FreeCodeCamp
and deep-dived into their video tutorial (https://www.youtube.com/watch?v=PkZNo7MFNFg)
read the book "A smarter way to learn Javascript" by Mark Myers
I have to credit all of these for finally getting there, where I needed to be in my understanding of this language.

GIFs and pictures
The credit for the gifs goes to GIPHY.

Woman Legs GIF for "seconds" overlay https://giphy.com/gifs/woman-legs-2j5Jj6bjfNJLy
Black And White Brooks GIF for "lost" overlay https://giphy.com/gifs/brooks-louise-736he3qcXJhwQ
Oh Dita Take Me Now GIF for "victory" overlay https://giphy.com/gifs/dita-von-teese-oh-take-me-now-p09nbHVNTYn6
The credit of the drawn images on the cards goes to AnnaliseArt on Pixabay.com

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
-*week menu shuffle
-add 10 recp. per country
-*value in stars option? No
-*list ingredients!
=*cancel button @ add recipe, and edit profile, and edit password
-*search function @ recipes page
-*pop up before deleting recipy or profile
*-ingredients field big enough for text (textarea)
*-log out when deleting profile (bug) 
-*delete all recipes of profile?
-*backend defensive programming
=*change url to slug
-write readme


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



-autocomplete for search
-url to slug in profile bug
-could not build route from delete recipe and delete profile-could not build route from cancel buttons (url slug bug)
-delete recipe 
-check flash styling
-already extisting username sign in sign up could not build route 

-remove session cookie when deleteing profile

-bug to fix: mobile friendly alert message