# Milestone 4 Project - M P H Photography
 
Live application demo can be found [**here**](https://ms4-project-mph.herokuapp.com/)
 
## Table of Contents
 
1. [UX](#UX)
   * [Application overview](#Application-overview)
   * [User stories](#User-stories)
   * [Design choices](#Design-choices)
   * [Database Schema](#Database-schema)
   * [Wireframes](#Wireframes)
2. [Features](#Features)
   * [Existing features](#Existing-features)
   * [Future features](#Future-features)
3. [Technologies Used](#Technologies-Used)
4. [Testing](#Testing)
   * [Implemented features](#Implemented-features)
   * [Functionality](#Functionality)
   * [Bugs](#Bugs)
5. [Deployment](#Deployment)
6. [Credits](#Credits)
   * [Content sources](#Content-sources)
   * [Acknowledgements](#Acknowledgements)
 
 
_____
 
## UX
 
### Application overview

For my MS4 project I have designed a fictional e-commerce and photography services website. This is a full stack, fully responsive application, designed to showcase a photographer’s skills through a range of available-to-purchase prints and a portfolio of previous client work.
 
### User stories
* 
* 
 
### Design choices
* 

### Database schema
![Database Schema](https://github.com/MichaelpHann/MS3-Project/blob/master/static/README-imgs/Database%20Schema.PNG)

This project has been built using MongoDB Atlas. MongoDB is a non-relational database that enables the storage and retrieval of user data sent to the database.

The database schema illustrated above is relatively simple, containing three collections, each of which contain two or more documents.

* **Categories Collection** - includes reference to the category name, only. The app includes a number of preset categories, and the "Admin" user has the ability to add additional categories via the "Create Category" function.

* **Posts Collection** - includes user inputs as well as data injected/retrieved from other collections. The user's form inputs when creating the blog post are strings and populate "post_title" and "post_content" documents. The "created_by" document is a string and is populated with the username from the **Users Collection**. The "poster" document is populated with the user's ObjectId from the **Users Collection**. The "favourites" document is an integer that increments or decrements each time a user adds or removes a post from their favourites.

* **Users Collection** - also includes user inputs as well as data injected/retrieved from other collections. Inputs from the user sign-up form will be the first posting of the "first_name", "last_name", "username" and "password" string documents. These will be accessed/referred to each time the user signs into the app as well as if the user publishes a post. The "user_posts" document is an array and stores the ObjectId of each blog post that the user publishes. This array will be accessed and rendered to the user's profile page, displaying each of the user's posts. The "fav_posts" document is also an array and stores the ObjectId of each blog post that the user 'likes'. This array will be accessed and rendered to the user's profile page, displaying each of the user's "favourited" posts.
 
### Wireframes
Wireframes for this website can be accessed in my wireframes folder within this github repository - [my wireframes](https://github.com/MichaelpHann/MS3-Project/tree/master/Wireframes)
 
_____

## Features
### Existing features

###### User status-dependent Navbar/Ribbon
Options that a user will see displayed in the navbar are dependant on the user’s status (logged in, logged out, logged in & Admin user status).

Users that are not logged in will see:
- Home
- Sign In
- Sign Up

Users that are logged in will see:
- Home
- Explore
- Profile
- New Post
- Sign Out

User with Admin status who is logged in will see:
- Home
- Explore
- Profile
- New Post
- Manage Categories
- Sign Out

###### Homepage
The landing page presents a simple narrative introduction/background to the application. Additionally, a user who is not logged in will be presented with **Sign In** and **Sign Up** buttons that they can select depending on whether they are a new or existing user. A user who is already logged in will be presented with an **Explore** button that will direct them to the **Explore** page when pressed.

###### Create account
A new user can create their own profile by selecting the **Sign Up** button on the Navbar. The user must enter their first name, last name, a username and password to create an account. There is a check in place to ensure the proposed username does not already exist on the database. There are also checks in place to ensure the username and passwords are of appropriate min and max lengths, and only contain acceptable characters. The Werkzeug package takes the input from the password form and generates a hashed password. This provides far greater security than storing passwords in plain text. The users new profile will be added to the **Users Collection** on MongoDB. A flash message will welcome the user.

###### Sign In
Users who have created an account can log into their own profile by selecting the **Sign In** button on the Navbar. The user must enter their Username and Password as stored in the database to log in, otherwise they will be presented with a message indicating that one or both elements are incorrect. A flash message will welcome the user back.

###### Sign Out
Users that have signed into the site can end their session at any time by clicking the **Sign Out** button on the Navbar. Flask will end their session using the session.pop() method and will redirect the user to the **Sign In** page.

###### New Post
A registered user who is signed into the application can create a new blog post by selecting the **New Post** button on the Navbar.

The user must complete all elements of the **New Post** form including selecting a Category from the pre-populated dropdown menu, adding a blog post title and blog post content. The user will be prompted to complete all fields if they try to publish the post without them all having been completed. The published post will be stored in the **Posts Collection** in MongoDB, with the ObjectId also stored in the **user_posts** document of the specific user in the **Users Collection**. The post will be displayed on both the **Explore** page and the **USER POSTS** tab of the user’s **Profile** page (see detail below). A flash message will confirm the post was successfully published.

###### Edit Post
A registered user who is signed into their profile and who has published a post can edit their post by selecting the **Edit** button.

The user can click this button when viewing their posts on either the **Explore** or **Profile** page. The user will be taken to the **Edit Post** page where any/each of the three form elements - Category, Post Title, Post Content - can be changed. Once the user confirms the changes the edited post will be stored in the **Posts Collection** on MongoDB, and the changes will be displayed on both the Explore and Profile pages. A flash message will confirm the post was successfully updated. Access restrictions mean a user cannot edit another user’s post. 

###### Delete Post
A registered user who is signed into their profile and who has published a post can delete their post by selecting the **Delete** button.

The user can click this button when viewing their posts on either the **Explore** or **Profile** page. The post will be deleted from the **Posts Collection** in MongoDB and the ObjectId will be removed from the the **user_posts** document in the **Users Collection** also. Additionally, the post will no longer be displayed on either the **Explore** or **Profile** pages. A flash message will confirm the post has been deleted. Access restrictions mean a user cannot delete another user’s post. 

###### Like Post / Unlike Post
A user can “like” or “favourite” any post by clicking on the heart icon in the bottom-right of the post. Once clicked, the **favourites** document of the post in the **Posts Collection** in MongoDB is incremented by 1. Additionally, the ObjectId of the post is added to the “fav_posts” of the specific user in the **Users Collection** in MongoDB. Finally, the colour of the icon will change and the post will be added to the users **FAVOURITE POSTS** tab on their **Profile** page.

If the user clicks the same icon again, return it to its original colour, the exact reverse of events described above will occur.

###### New Category
The registered user with the **Admin** username, who is signed into the application can create a new category by selecting the **Manage Categories** button on the Navbar.

The user will be brought to the **Manage Categories** page where they can then select the **Create Category** button. They will be taken to the **New Category** page where they can add a new category name. A flash message will confirm the new post has been created. Once created, the category will be added to the **Categories Collection** on MongoDB and will be available to all users in the pre-populated dropdown menu in the **New Post** page. Access restrictions prevent a user who is not the “Admin” user from creating a new category.

###### Edit Category
The registered user with the **Admin** username, who is signed into the application can edit an existing category by selecting the **Manage Categories** button on the Navbar. 

The user will be brought to the **Manage Categories** page where each existing category will have a corresponding **Edit** button. When selected the user will be taken to the **Edit Category** page where they can amend the category name. A flash message will confirm the the category name has been updated. The amended category will be stored in the **Categories Collection** on MongoDB. Once updated, the revised category will be available to all users in the pre-populated dropdown menu in the **New Post** page. Access restrictions prevent a user who is not the **Admin** user from creating a new category.

###### Delete Category
The registered user with the **Admin** username, who is signed into the application can edit an existing category by selecting the **Manage Categories** button on the Navbar.

The user will be brought to the **Manage Categories** page where each existing category will have a corresponding **Delete** button. Once clicked the post will be deleted from the database, and its ObjectId is removed from their list of posts in their user record. The recipe is also removed from the favourites of all other users.

###### Profile - User Posts
All posts that a user has published will be displayed in the **USER POSTS** tab of their **Profile** page. The user can edit and delete these posts in the same manner as they can on the **Explore** page.

If the user has not published any posts they will be presented with a placeholder message of **View all your published posts here!**.

Profile - Favourite Posts
All posts that a user has “liked” or “favourited” will be displayed in the **FAVOURITE POSTS**  tab of their **Profile** page.

If the user has not “liked”/“favourited” any posts they will be presented with a placeholder message of **A place for you to curate your favourite posts!**.

###### Explore - Search
Any user that is logged in can conduct a keyword search based on the words contained with the Post Titles and Post Contents, as displayed at any point in time on the **Explore** page. A successful search will result in only those posts that contain a word matching that which was searched displayed on the **Explore** page.

###### Explore - Posts
Any user that is logged in can view all posts that have been published at any point in time on the **Explore** page.

### Future features

###### Product detail image carousel
Introduce a carousel of images in each product detail page that shows the print “in real life”, e.g. hung on a wall. This will help to give the potential customer a better idea of how the print might look when hung in their own home/office.

###### Defensive delete functionality
Course submission time pressures meant I was unable to implement this feature. However, in order to avoid a superuser accidentally deleting a product or portfolio item, it would be helpful to have a confirmation modal that asks the user to confirm that they definitely want to delete a product or project.

###### Gift cards
Course submission time pressures meant I was unable to implement this feature. However, the underlying basis has been included in the DB schema. Included in the products model is an ‘is_digital’ class. The thinking here was with a view to providing gift cards, i.e. that a site user could purchase a gift card for someone. The gift card would come in two forms - one a physical gift card (‘is_digital’ set to False) and the other an e-gift card that could be emailed to the user (‘is_digital’ set to True). If the only product in the customers shopping bag/checkout was an e-gift card the the user’s postal address details would not be displayed/they would not have to fill them in to complete the order.

###### Social login
The ability for users to sign up/sign in via their preferred social media channel, providing a more seamless, integrated user experience.
_____
 
## Technologies Used
#### Coding Languages
* [HTML5](https://en.wikipedia.org/wiki/HTML5) - used to build the structure of this application.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - used for styling of the application.
* [Python](https://www.python.org/) - an interpreted, high-level, general-purpose language, used for all backend functions of this project.
* [Django](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [JavaScript](https://www.javascript.com/) - used to provide application interactivity.

#### Integrations & Frameworks
* [Stripe](https://stripe.com/en-gb) - Stripe API allows users to make and receive payments over the internet.
* [jQuery](https://www.javascript.com/) - used to provide application interactivity and simplify DOM manipulation.
* [Materialize CSS](https://materializecss.com/) - used to provide responsive frontend framework.
* [Google Fonts - Material Icons](https://fonts.google.com/icons) - used to style the application icons.
* [Font Awesome](https://fontawesome.com/) - used to style the application icons.

#### Version Control, Storage & Hosting
* [GIT](https://git-scm.com/) - used GitPod for version control.
* [GitHub](https://github.com/) - used for hosting the repository.
* [Heroku](https://heroku.com/) - used to deploy the live application.
* [Amazon S3](https://aws.amazon.com/aws/s3) - Amazon Simple Storage Service is a service offered by Amazon Web Services, providing object storage through a web service interface.

#### Database Management System
* [Heroku Postgres](https://www.heroku.com/postgres) - a popular open source relational database management system.
 
#### Testing tools
* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) to test the device responsiveness of the application.
* [JSHint](https://jshint.com/) to validate the JavaScript code.
* [JSLint](https://jshint.com/) to validate the JavaScript code.
* [Esprima Syntax Validator](http://esprima.org/demo/validate.html) to validate the Javascript code.
* [W3C CSS validation](https://jigsaw.w3.org/css-validator/) to validate CSS. 
* [W3C Markup Validation](https://validator.w3.org/) to validate HTML code.
* [Auto-prefixer](https://autoprefixer.github.io/) to ensure the css includes all necessary browser prefixes it needs.
* [PEP8 Online Validator](http://pep8online.com/) to ensure the Python code is fully PEP8 compliant.
 
## Testing
#### Code Validation

###### HTML
The [W3C Markup Validator](https://validator.w3.org/) was used to check HTML from all templates. This generated a number of errors due to the inability of the validator to understand Jinja templating that builds most aspects of each page. For the HTML that does not involve Jinja, no errors were found.

###### CSS autoprefixer
The online [CSS autoprefixer](https://autoprefixer.github.io/) was used to ensure all appropriate prefixes were included. Output generated was used.

###### CSS
The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to check all CSS code, with no errors found.

###### Javascript
All Javascript was passed through the [Esprima Syntax Validator](http://esprima.org/demo/validate.html) and was found to be syntactically valid.

###### Python
All Python code was passed through the [PEP8 Online Validator](http://pep8online.com/) and is fully PEP8 compliant.


#### Manual testing
Significant iterative manual testing was conducted on this application throughout the development process. Testing was conducted to ensure application functionality and responsiveness across a range of browsers and devices.

The outcome of the manual testing performed is documented [here](https://github.com/MichaelpHann/MS3-Project/tree/master/testing).
 
#### Functionality
Google Chrome Developer was the principal tool used throughout the build to test functionality and device responsiveness. Additionally, in the latter stages, application responsiveness was tested via live user testing across a range of mobile, tablet and desktop devices. All feedback provided as part of this testing has been considered and, where necessary, incorporated into the application.

_____

_____

## Deployment
 
The following should be installed before deploying this application:
* [Python 3](https://www.python.org/)
* [PIP](https://pip.pypa.io/en/stable/installing)
* [GIT](https://www.atlassian.com/git/tutorials/install-git)
* A suitable IDE, such as [Microsoft Visual Studio Code](https://code.visualstudio.com)

The app also relies on the following services, each of which should have an account created:
* [Amazon AWS](https://aws.amazon.com/)
* [Stripe](https://stripe.com/)
* An email account, [GMail](https://mail.google.com/) is ideal as it is reliable and easy to set up.

#### Local Deployment
1. To clone this respository on GitHub navigate to the project [here](https://github.com/MichaelpHann/MS4_MPHPAD), select the **Code** dropdown button and download the zip of the project.
* Alternatively, enter the following into the Git CLI terminal:
```
git clone https://github.com/MichaelpHann/MS4_MPHPAD.git
```

2. Access the folder in your terminal window and install application’s required files using the following command:
```
pip3 install -r requirements.txt
```

3. Create an `env.py` file containing the following environment variables:
```
AWS_SECRET_ACCESS_KEY
AWS_S3_CUSTOM_DOMAIN
DATABASE_URL
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
SECRET_KEY
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
USE_AWL
```

Ensure the `env.py` file is added to `.gitignore` prior to making any commits.

NB. A working knowledge on how to configure a publicly accessible S3 Bucket and the Stripe API are assumed for this project, as detailed instructions are beyond the scope of this document.

4. At the terminal prompt, type `python3 manage.py runserver`. Django should begin to run a development server and the application will be available in your browser at the address `http://localhost:8000`.

Running the project for the first time will cause Django to create a SQLite3 database, entitled `db.sqlite3`. At the terminal prompt, the following command should be entered to create the database schema (as illustrated earlier in this file).
```
python3 manage.py migrate
```

5. Create a superuser in order to access the admin functionality, as follows:
```
python3 manage.py createsuperuser
```


#### Remote Deployment

To deploy this application to Heroku, the following steps must be followed:

1. Create a `requirements.txt` file to enable Heroku to install the required dependencies to run the app.
```
pip3 freeze —local > requirements.txt
```
2. Create a `Procfile` to tell Heroku the type of application that is being deployed and how to run it.
3. In Heroku, select the **New** dropdown button on the right-hand-side and select **Create new app**.
4. On the application dashboard in Heroku, select the **Deploy** tab and then select **GitHub** as the deployment method to connect the application to your GitHub repository.
5. In **Resources** tab, navigate to the Add-ons section and add the Heroku Postgres add-on. The hobby level should be selected when prompted.
6. In the **Settings** tab, click the **Reveal Config Vars** button to configure environment variables (the same environment variables as listed in **Local Deployment** above.
7. The application will be deployed and built by Heroku and availably to view via the **View App** button.
8. Alter your project’s `settings.py` file to connect to the remote database using the `dj_database_url` Python package.
9. The same steps set out in **Local Deployment** above should be followed to migrate the schema to the remote database.

_____

## Credits
### Technical sources
* Technical elements of the project were developed and, as required, adapted based on frameworks implemented in the [Code Institute Boutique Ado mini-project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/)
* The homepage workflow section structure was built in line with, and adapted where appropriate, guidance from [The Net Ninja](https://www.youtube.com/watch?v=KaP_t0RrAS8&list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff&index=18)
* The contact form was built in line with, and adapted where appropriate, guidance from [Ordinary Coders](https://www.ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend)
* The messages banner background colour was styled using [Coolors](https://coolors.co/) gradient maker

### Media
* All images throughout the application were sourced from either [Pexels](https://www.pexels.com/) or [Unsplash](https://unsplash.com/) and, where required, resized using [Canva](https://www.canva.com/)

_____

### Acknowledgements
I would like to thank both [Felipe Alarcon](https://github.com/fandressouza) and [Chris Quinn](https://github.com/10xOXR) for their guidance and constructive feedback throughout the project.
 
