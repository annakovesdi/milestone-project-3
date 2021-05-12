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
11. As a user, i want to log out

Visitors find the experience they are searching for because:

This site is colourful and attractive. It is very easy to use and provides the millenial or z-generation hero with an answer to the 
most grinding question in adulting: 

>"How can I decide what to eat tonight, every night, for the rest of my life?"

With the week menu shuffle, in just one click, you solved a huge everyday problem and have energy left for other crucial stuff: like getting a mortgage. 

## Wireframes

![Index html mobile](/static/img/wireframes/index-html-mobile.png "index html mobile")
![Index html](/static/img/wireframes/Index-html.png "index html")
![Recipe one mobile](/static/img/wireframes/recipe-one-mobile.png "recipe one mobile")
![Recipe one](/static/img/wireframes/recipe-one.png "recipe one")
The desktop site did not need two pictures, because asking two pictures from a user was excessive. 
![Search mobile](/static/img/wireframes/search.png "search mobile")
![search](/static/img/wireframes/search-big.png "search")
(I decided not to make a carousel for the search button because the site was already quite busy as is. It would have been overkill for the senses 
to add a carousel for seach items.)
![Sign up mobile](/static/img/wireframes/sign-up-mobile.png "sign up mobile")
![Sign up](/static/img/wireframes/sign-up.png "sign up")


## Features

The colorful site features a heading picture on every main page and:

 - **Index** page, with three aggregated recipes from the database and a link to the week-menu-shuffle feature
 - **Week Menu Shuffle** page, where a dropdown with flags of all countries of the world lets the user select 
 a country of choice, and then aggregates seven recipes from that country from the database (if that many recipes are avaliable- for the moment only Italy has seven recipes in the db)
 - **Recipes** page with all recipes displayed of the db, and a search field where the user can search in the data base in recipy name, ingredients, discription and country
 - **Recipe** page where a recipe is readable in it's entirety. If the user is the creator of the recipy, it is also possible to edit or delete it
 - **Sign Up** page where the user can sign up providing a first name, username, password and email address
 - **Log In** page where an existing user can log in
 - **Log Out** When clicked a logged in user logs out
 - **Profile** page where the logged in user can see their recipes and edit their name, password, email address or delete the profile and all recipes
 - **Add recipe** page where the user can add a recipe to the database

### _Features to implement in the future:_

Oh so may, so many. 

- allow tracking cookies alert
- forgotten password reset 
- automatic email welcoming the new user
- recipe ratings
- recipe comments
- autofill on search field with only words that occur in the database
- search on best rated recipes
- week menu shuffle does not only take the country in consideration, but also the ingredients. Like this economic shopping is possible
- auto generated shopping list for your week menu
- categorizing recipes by meal, amount of calories, time to prepare etc
- users can follow interesing users

And actually the options are endless! It would be fun to create a social recipe site, where blog posts and pretty pictures by the users 
would make it a fun place to browse even when you are not cooking. Foodporn all day every day! The more time users spend on the site, more money ads would make.
All of this was a bit beyond the scope of learning these basics, but if i have time i would gladly continue to shape this. 
I miss somethink like this in my life.

## Technologies used
- Gitpod to develop the website
- GitHub for version control and code hosting
- Heroku for deployment
- MongoDB as database
- Google fonts for the fonts
- Plugin CountrySelect for the country dropdown
- Html, Css, JavaScript and Python are the developing languages
- Frameworks: Flask for templates, Materialize for CSS, JQery for JavaScript
- Balsamiq for the wireframes
- lambdatest.com for static testing
- Chrome dev tools for manual testing

## Testing
Testing information can be found in the [TESTING.md](TESTING.md "Testing") file

## Deployment
The site is deployed through Heroku.

Steps to setup Heroku deployment:

- The Heroku Command Line Interface (CLI) makes it easy to create and manage Heroku apps directly from the terminal. 
It’s an essential part of using Heroku and requires Git, the popular version control system. If you don’t already have Git installed, complete the following before installing the CLI: 
[Git Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [First-time Git setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

- [Install the CLI according to your OS](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
For macOS this is **$ brew tap heroku/brew && brew install heroku**

- To verify your CLI installation, use the heroku --version command

- Create a profile in the Heroku app in your browser

- After you install the CLI, run the heroku login command. You’ll be prompted to enter any key to go to your web browser to complete login. The CLI will then log you in automatically.
 
- Now you’re ready to create your first Heroku app. This app is called eatingtheworld and is created with the preferred language Python

- In the settings of the Heroku app in the browser Config vars are added, they change the way your app behaves. They are for eatingtheworld IP, The name and uri of the database, port and a secret key.

- Under the Deply tab of the Heroku app in the browser it is possible to connect a GitHub Repository to the Heroku app, and automatically deploy from the main branch. In this case every push to main will deploy a new version of this app. 
Deploys happen automatically: be sure that this branch in GitHub is always in a deployable state and any tests have passed before you push. 

- Before automatically deploying the app through GitHub make sure to create a Procfile. Heroku apps include a Procfile that specifies the commands that are executed by the app on startup. You can use a Procfile to declare a variety of process types, 
including: your app’s web server, multiple types of worker processes, a singleton process, such as a clock or tasks to run before a new release is deployed
Each dyno in your app belongs to one of the declared process types, and it executes the startup command associated with that process type. The Procfile is always a simple text file that is named Procfile without a file extension. [Click to know more about the Procfile](https://devcenter.heroku.com/articles/procfile)

- Before automatically deploying the app through GitHub make sure to create a requirements.txt file by typeing $ pip freeze > requirements.txt. In short,
 we generate and share requirements.txt files to make it easier for other developers to install the correct versions of the required Python libraries (or “packages”) to run the Python code we’ve written. To
 install the required files just run $ pip install -r requirements.txt in your terminal. [Click for more information on requirements.txt](https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e)

- Be sure to create a .gitignore file that hides sensitive information from deployment. Always check with $ git status that your sensitive files are not pushed to GitHub and Heroku. A gitignore file specifies intentionally untracked files that Git should ignore.
[Click to read more about .gitignore](https://git-scm.com/docs/gitignore)

- Be sure to change debug=True to debug=False in your python file before deployment. 

The site is now live at https://eatingtheworld.herokuapp.com/

## Credits

Most of the credits this learning season go to Code Institute. By reviewing the mini projects I created alot of this site. 
Ofcourse there were lots of other helpers too. They are listed here in no particular order.

- Read the book "A smarter way to learn Python" by Mark Myers
- Documentation [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- Documentation [Materialize](https://materializecss.com/)
- Tutorial [PyMongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/#filters) stuff
- Tutor Tim for helping me with the aggregate 3 recipes on index.html
- Tutor Igor for helping me create the code in Python for "week_menu" (and getting there from "week_menu_shuffle" by tutor Jo)
- Mentor Victor for explaining how to make sure a user is logged in
- Countryselect Plugin created by the amazing mrmarkfrench from https://www.jqueryscript.net/form/country-picker-flags.html
- How to check if the search had no results (https://www.geeksforgeeks.org/how-to-check-if-the-pymongo-cursor-is-empty/)
- How to partially update in DB How to partially update in db https://stackoverflow.com/questions/10290621/how-do-i-partially-update-an-object-in-mongodb-so-the-new-object-will-overlay answer Eran Medan


### Header Images

All header images are credited to [Unsplash](https://unsplash.com/). The names of the photographers are: 
- paprika.jpg Heijo Reinl
- bread.jpg Ken Lawrence
- citrus.jpg Luke Michael
- basic.jpg Dan Gold
- veggie.jpg Sven Scheuermeier
- market.jpg Julian Hanslmaier
- fruit.jpg Roman Davayposmotrim
- pepper.jpg webvilla
