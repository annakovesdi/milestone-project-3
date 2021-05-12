# Testing

## Validation

I put the code through various validators. The HTML in [W3C](https://validator.w3.org/). 
I fixed all the red ones, but let the yellow warnings for sections without heading in these particular cases exist.

![Html Validation](/static/img/validator/html1.png)

![Html Validation](/static/img/validator/html2.png)

![Html Validation](/static/img/validator/html3.png)

![Html Validation](/static/img/validator/html4.png)

![Html Validation](/static/img/validator/html5.png)

![Html Validation](/static/img/validator/html6.png)

![Html Validation](/static/img/validator/html7.png)

![Html Validation](/static/img/validator/html8.png)

![Html Validation](/static/img/validator/html9.png)

![Html Validation](/static/img/validator/html10.png)

![Html Validation](/static/img/validator/html11.png)

The css validator of w3c CSS validator found 2 errors that i did not fix, since they are relevant. They give the buttons 
on the profile of a user shadow when hovered over.

![CSS Validation](/static/img/validator/css.png)

## Visitor stories testing

1. As a new visitor, I want to easily find my way to a recipe.

When arriving on the site, immedietly 3 recipes are displayed. they are aggregated from the database, this means they keep changeing after a refresh. 
When clicking on the plus button of a recipe, you can see this recipe entirely.

2. As a new visitor, I want to be able to search in the recipe for a dish, a country or an ingredient. 

By clicking on the button recipes, the user can find the search field. The search field is an index of most words in the database in the keys recipe name, description, country and ingredients. 
Under the search field all recipes are displayed on deafult. 
When a search querie has been made and the search has results, the results are displayed under the search box. If a search has no results a flashed massege appears, 
explaining that the search has no results, and all recipes are displayed under the search field.

3. As a new visitor, I want to sign up. 

By clicking the sign up button, a form appears requesting first name, username, email address and password. If all fields are validated
green the user is signed up and logged in. They get redirected to their profile page, see a flash message welcoming them and can use this username and password combination to log in next time they visit the site.

4. As a returning visitor, I would like to log in.

When a user is signed up and still can remember their username and password they can log in by filling in the form under the log-in button. 
They get redirected to their profile page and see a flash message that they have been logged in. 

5. As a user, i would like to see my profile and my added recipes.

On the profile page the user can see their first name, 

6. As a user, i would like to edit my profile information and/or my password.
7. As a user, i would like to add a recipe.
8. As a user, i would like to edit or delete my recipe.
9. As a user, i would like to delete my profile and all my recipes. 
10. As a true enthausiast, i would like the site to create a country themed week menu for me.
11. As a user, i want to log out

## Manual (logical) testing of all elements, functionality

Step by step, I will guide you through the page, and describe bugs that I fixed and the functionality of the finished site.

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

## defensive strategies

## Testing across browsers and devices




defensive strategies

problems: 
did not show image. put url instead of image_url and it did not render correctly.
could not insert new user, wrong name tags in html

recipe url no special characters allowed, spaces replaced with -, lower


https://stackoverflow.com/questions/10290621/how-do-i-partially-update-an-object-in-mongodb-so-the-new-object-will-overlay answer Eran Medan
How to update only some fields bug

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






-autocomplete for search
-url to slug in profile bug
-could not build route from delete recipe and delete profile-could not build route from cancel buttons (url slug bug)
-delete recipe 
-check flash styling
-already extisting username sign in sign up could not build route 

-remove session cookie when deleteing profile

-bug to fix: mobile friendly alert message