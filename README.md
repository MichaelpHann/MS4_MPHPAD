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
* As a new user I want to be able to quickly and intuitively understand the purpose of the website, how to navigate throughout it, and what I need to do to register and fully utilise the functionality on offer.
* As a user I want to be able to quickly see who the website owner/photography is, learn about their experience and understand what services they offer.
* As a user, potentially interested in hiring the photographer, I want to be able to easily view a portfolio of a selection of their previous work to allow me to determine if I like it and their style of working.
* As a user I want to be able to easily locate the website's shop and effortlessly browse through the selection of prints for sale, being able to understand their size and pricing.
* As a profile user who wishes to purchase a print I want a straight forward and intuitive checkout process.
* As a profile user I want to be able to save/store my personal and delivery information to allow even further ease of use of the website in the future.
* As a user I want to be able to contact the site owner/photographer if I have a question about a product or service.
* As a site owner and photographer I want to be able to effectively showcase my prints for sale, previous experience and highlight my services on offer.
* As a site owner I want to be able to effectively and efficiently manage the stock available in the website's shop and the images I have on display in my portfolio of work, including being able to add, edit and delete products/portfolio items.

### Design choices
* The website has been designed using the Materialize framework, utilising the framework's standard elements, with the colour altered to match the overall scheme of the website.
* There is a simple, clean white core colour scheme used throughout the website. This design choice was based on wanting to ensure a user's eye was drawn to the images, as they are the USP of the website/photographer. I didn't wany anything to detract from them.
* There is a minimalist, yet extremely functional, user interface on the navigation bar/ribbon, that collapses for mobile functionality. Again, I thought it important that the design focused on drawing the user's eye to the images throughout.
* For website pages that do not include any images I have maintained the simple white colour palette. I considered adding other colours in these intances, however on balance I felt the pages worked well and thought it was more important to maintin a consistent colour scheme throughout.
* The Karla font from Google Fonts was used throughout the website. This was principally displayed using a 300 font-weight and it most suited the clean, simple overall deisgn theme.
* Use of instructive/complementary actions icons throughout. Consistent use of minimalist “chevron” icons used in buttons throughout, except for small number of distinct action buttons.
* Descriptive button labelling throughout to ensure a positive user experience.
* Distinctive and complementary button colour scheme used throughout. Other than the images these are the only "splash" of colour in the website. The colours have attempted to be utilised consistently throughout with. For example, "return" actions like to keep shopping, adjust page or go to the homepage, have been coloured consistently. Then, "call to action" buttons such as add to bag and complete order have been styled in consistent colour.

### Database schema
![Database Schema](https://github.com/MichaelpHann/MS4_MPHPAD/blob/master/static/README_imgs/MS4%20DB%20Schema.png)

This project has been built initially using the SQLite3 database, before finally migrating to utilise Heroku Postgres. Heroku Postgres is a popular relational database.

The database schema illustrated above is relatively simple, based on four applications, each containing one or two models.

### Wireframes
Wireframes for this website can be accessed in my wireframes folder within this github repository - [my wireframes](https://github.com/MichaelpHann/MS3-Project/tree/master/Wireframes)
 
_____

## Features
### Existing features

###### User status-dependent Navbar/Ribbon
Options that a user will see displayed in the navbar are dependant on the user’s status (signed up, signed out, signed in & Superuser status).

Users that are not signed in will see:
- Portfolio
- Shop
- Contact
- M P H Photography icon and homepage link
- Sign Up
- Sign In
- Shopping basket icon and basket total

Users that are signed in will see:
- Portfolio
- Shop
- Contact
- M P H Photography icon and homepage link
- Account dropdown button that includes Profile and Sign Out options
- Shopping basket icon and basket total

User with Superuser status who is logged in will see:
- Portfolio
- Shop
- Contact
- M P H Photography icon and homepage link
- Account dropdown button that includes Profile, Sign Out, Product Admin and Project Admin options
- Shopping basket icon and basket total

###### Homepage
The landing page is structured with distinct narrative sections throughout. The first section is a large 3-image slider/carousel. There is an "in page" link included to direct the user to descriptions of the photographer's services on offer. There is also a "Get In Touch" button that directs the user to the Contact page. The two parallaxes offer effectively separation of the narrative sections.

###### Create account
A new user can create their own profile by selecting the **Sign Up** button on the Navbar. The code checks the database for existing users to ensure to proposed username is unique. There are also checks in place to ensure the username and passwords are of appropriate min and max lengths, and only contain acceptable characters.

###### Sign In
Users who have created an account can log into their own profile by selecting the **Sign In** button on the Navbar. The user must enter their Username and Password as stored in the database to log in, otherwise they will be presented with a message indicating that one or both elements are incorrect.

###### Sign Out
Users that have signed into the site can end their session at any time by clicking the **Sign Out** button on the Navbar. They will be prompted to confirm that they want to sign out by clicking the “Sign Out” button. Django will end their session and redirect the user to the homepage.

###### Portfolio
Users can click the **Portfolio** button in the Navbar to access the portfolio page. The page will render a responsive grid of all projects currently stored in the database. The user can hover over each image to see more detail. The date and location of when/where the image was captured is disclosed below each image. The user will be able to filter the projects displayed based on their category type.

###### Portfolio Admin - Edit a Project
A user with superuser access will have the ability to click an **Edit** button located beneath each portfolio item. They will be redirected to a page with a form pre-populated with the portfolio details. The superuser can amend any details in this form and save them by clicking the **Update Project** button. These changes will be stored in the database and the superuser will be redirected to the **Portfolio** page, with the changes made now displayed.

###### Portfolio - delete project
A user with superuser access will have the ability to click a **Delete** button beneath each portfolio item. This will delete the project from the database and re-render the Portfolio page, now excluding the deleted project.

###### Portfolio Admin - Add a Project
A user with superuser access will have the ability to select the **Portfolio Admin** option within the **Account** dropdown in the Navbar. They will be redirected to a page with a form with required project input fields. The superuser can add a project by populating this form, including adding an image, and save it by clicking the **Add Project** button. The new project will be stored in the database and the superuser will be redirected to the **Portfolio** page, with the new project will now be displayed.

###### Shop
Users can click the **Shop** button in the Navbar to access the shop page. The page will render a responsive grid of all products currently stored in the database. The size and price of each product is disclosed beneath each product image. Each product image is clickable and will direct the user to the corresponding Product Detail page. On the Shop page, the user will be able to filter the products displayed based on their category type.

###### Product Admin - Edit a Product
A user with superuser access will have the ability to click an **Edit** button located beneath each product. They will be redirected to a page with a form pre-populated with the product details. The superuser can amend any details in this form and save them by clicking the **Update Product** button. These changes will be stored in the database and the superuser will be redirected to the **Shop** page, with the changes made now displayed.

###### Shop - delete product
A user with superuser access will have the ability to click a **Delete** button beneath each product. This will delete the product from the database and re-render the **Shop** page, now excluding the deleted product.

###### Portfolio Admin - Add a Product
A user with superuser access will have the ability to select the **Product Admin** option within the **Account** dropdown in the Navbar. They will be redirected to a page with a form with required product input fields. The superuser can add a product by populating this form, including adding an image, and save it by clicking the **Add Product** button. The new product will be stored in the database and the superuser will be redirected to the **Shop** page, with the new product will now be displayed.

###### Product detail page
Users, having clicked on a product image in the **Shop** page, are redirected to the product’s corresponding detail page. Further information about the product is disclosed here. The user can select a specified quantity of the product and add it to the shopping bag. The shopping bag feature in the Navbar will be updated to reflect the total cost of the products added, i.e. Price x Quantity. There is a restriction in place preventing a zero or negative quantity being selected. The user can also return to the Shop page by selecting the **Keep Shopping** button.

###### Shopping Bag
Users can access the shopping bag by clicking the shopping bag icon/total order value in the Navbar. The user will be presented with a detailed summary of all products added to the shopping bag. The user can adjust the quantity of each product in the shopping bag (down to 1 or up to 99 items) by clicking the plus and minus icon buttons and confirming the new quantity be clicking **Update**. There is a restriction in place preventing a zero or negative quantity being selected. The total order cost will be adjusted automatically to reflect any changes in quantities. To remove a product entirely, the **Delete** button for the specific product should be pressed. This will delete the product from the shopping bag and update the total order value accordingly. The **Keep Shopping** button redirects the user to the **Shop** page. The **Secure Checkout** button will direct the user to the **Checkout** page.

###### Checkout
Users are presented with an *Order Summary** showing details and price of the purchase in progress. Users are also presented with a form to be completed in order to finalise the order. Some fields, such as Full Name, Address Line 1, etc, are required and form validation errors will flag any missing inputs if the user attempts to process the order without them. If the user has a profile and has previously requested, by clicking the relevant checkbox ,for their details to be saved then this form will be pre-populated. If not pre-populated, a user can click the checkbox input at the bottom of the form to save the information to their profile. The user can enter their card details and finalise the purchase by pressing the **Complete Order** button. The completed order will be registered on the site owners Stripe profile and an order confirmation email will be sent the the customers email address.

###### Checkout Success
On completing their order the user is directed to an order summary page that includes confirmation of the email address to which the order summary email will be sent.

###### Contact
Users can access the messaging/email functionality by clicking the **Contact** link in the Navbar. The user is presented with a form with required input fields. When the **Send** button is pressed the message is sent to the site owner/registered email address and the user is redirected to an email success page.

###### Email success
The user will receive confirmation here that their email has been sent.

###### Other user administrative features
There are several other user administrative features within the site including password reset functionality and email confirmation/verification.

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
The [W3C Markup Validator](https://validator.w3.org/) was used to check HTML from all templates. This generated a number of errors due to the inability of the validator to understand Django templating logic that builds most aspects of each page. For the HTML that does not involve Django templating, no errors were found.

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

The outcome of the manual testing performed is documented [here](https://github.com/MichaelpHann/MS4_MPHPAD/tree/master/testing).
 
#### Functionality
Google Chrome Developer was the principal tool used throughout the build to test functionality and device responsiveness. Additionally, in the latter stages, application responsiveness was tested via live user testing across a range of mobile, tablet and desktop devices. All feedback provided as part of this testing has been considered and, where necessary, incorporated into the application.

#### Bugs
There is an inconsistency between device types with the required mouse pointer position when clicking the three Checkbox inputs in the application. There is no issue on mobile devices, the user can press directly onto the Checkbox. However, the user most click just to the left of the Checkbox when using the application on a desktop. Project submission timelines did not allow me the time to resolve this issue.
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

### Local Deployment
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

### Remote Deployment

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
* Technical elements of the project were developed and, as required, adapted based on frameworks implemented in the [Code Institute Boutique Ado mini-project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/).
* The homepage workflow section structure was built in line with, and adapted where appropriate, guidance from [The Net Ninja](https://www.youtube.com/watch?v=KaP_t0RrAS8&list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff&index=18).
* The contact form was built in line with, and adapted where appropriate, guidance from [Ordinary Coders](https://www.ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend).
* The messages banner background colour was styled using [Coolors](https://coolors.co/) gradient maker

### Media
* All images throughout the application were sourced from either [Pexels](https://www.pexels.com/) or [Unsplash](https://unsplash.com/) and, where required, resized using [Canva](https://www.canva.com/).

_____

### Acknowledgements
I would like to thank both [Felipe Alarcon](https://github.com/fandressouza) and [Chris Quinn](https://github.com/10xOXR) for their guidance and constructive feedback throughout the project.
 
