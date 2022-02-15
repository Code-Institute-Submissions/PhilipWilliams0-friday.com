<h1 align="center">friday.com</h1>

[View the live project here.](https://friday-projects.herokuapp.com/)

friday.com is a site where users can log projects for completion with full CRUD functionality, using recently learned Python and Flask.  

<h2 align="center"><img src="https://github.com/PhilipWilliams0/friday.com/blob/main/static/img/responsive.png"></h2>

## **CONTENTS** ##

- [UX](#user-experience-(ux))
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Known Bugs](#known-bugs)
- [Deployment](#deployment)
- [Content](#content)
- [Media](#media)
- [Acknowledgements](#acknowledgements)



## User Experience (UX)

-   ### Project goals
This site is aimed at teams who want a free resource that will help them in their workday. It is also a site where users can share their projects with other departments. 

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to know about the site. 
        2. As a First Time Visitor, I want to easily create an account. 
        3. As a First Time Visitor, I want to be able to log a project.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to find information about projects.
        2. As a Returning Visitor, I want to be able to contact site owner. 
        3. As a Returning Visitor, I want to be able to edit or delete an project. 


    -   #### Frequent User Goals
        1. As a Frequent User, I want to able to change the status.
        1. As a Frequent User, I want to able to see my own projects. 

-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are Code Insititue purple, blue, and white.
    -   #### Typography
        -   The semi-rounded details of the letters give Lato a feeling of warmth, while the strong structure provides stability and seriousness.
    -   #### Imagery
        -   Imagery is important. The large, background hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.
    -   #### Data Schema

        -   Using MongoDB provides many benefits in the development of this app. Its flexible schema makes it easy to evolve and store data in a way that is easy to work with. MongoDB is also built to scale up quickly and supports all the main features of modern databases such as transactions.

        - Categories

                {   
                    "_id": ObjectId
                    "category_name": String
                }

        - Users

                {   "first_name": String
                    "last_name": String
                    "username": String
                    "password": String
                }

        - status

                {   
                    "_id": ObjectId
                    "status": String
                }

        - projects

                {
                    "_id": ObjectId
                    "category_name": String
                    "project_name": String
                    "project_description": String
                    "is_urgent": String 
                    "due_date": Date
                    "status_name": String
                }
                

        *   ### Wireframes

            -   Desktop Wireframe - [View](https://github.com/PhilipWilliams0/friday.com/tree/main/static/wireframes/desktop)

            -   Tablet  Wireframe - [View](https://github.com/PhilipWilliams0/friday.com/tree/main/static/wireframes/tablet)

            -   Mobile  Wireframe - [View](https://github.com/PhilipWilliams0/friday.com/tree/main/static/wireframes/mobile)

## Features

-   Responsive on all device sizes

-   Interactive elements which also display links on weather the user is signed in or anonymous. 

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

### Frameworks, Libraries & Programs Used

1. [Flask:](https://flask.palletsprojects.com/en/2.0.x/)
    - Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
1. [MongoDB:](https://www.mongodb.com/)
    - MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.
1. [Materialize 1.0.0:](https://materializecss.com/)
    - Materialize is a UI component library created with CSS, JavaScript, and HTML. Materialize UI components help in constructing attractive, consistent, and functional web pages and web apps, while adhering to modern web design principles such as browser portability, device independence, and graceful degradation.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [EmailJS:](https://www.emailjs.com/docs/tutorial/overview/)
    - EmailJS is a mail sending platform that directly sends an email without the requirement of code.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Heroku:](https://www.heroku.com)
    - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/PhilipWilliams0/friday.com/tree/main/static/wireframes) during the design process.
1. [EmailJS:](www.emailjs.com)
    - EmailJS helps to send emails using client-side technologies only. No server is required – just connect EmailJS to one of the supported email services, create an email template, and use our Javascript library to trigger an email.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to know about the site. 
        <h2 align="center"><img src="static/testing/user-stories/Screenshot 2022-02-15 at 09.48.20.png"></h2>
        1. 
    2. As a First Time Visitor, I want to easily create an account. 
        
        1. 
    3. As a First Time Visitor, I want to be able to log a project.
        
        1. 
       
-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find the new programming challenges or hackathons.

        1. These are clearly shown in the banner message.
        2. They will be directed to a page with another hero image and call to action.

    2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.

        1. The navigation bar clearly highlights the "Contact Us" Page.
        2. Here they can fill out the form on the page or are told that alternatively they can message the organisation on social media.
        3. The footer contains links to the organisations Facebook, Twitter and Instagram page as well as the organization's email.
        4. Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.
        5. The email button is set up to automatically open up your email app and autofill there email address in the "To" section.

    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
        2. Alternatively, the user can scroll to the bottom of the Home page to find the Facebook Group redirect card and can easily join by clicking the "Join Now!" button which like any external link, will open in a new tab to ensure they can get back to the website easily.
        3. If the user is on the "Our Favourites" page they will also be greeted with a call to action button to invite the user to the Facebook group. The user is incentivized as they are told there is a weekly favourite product posted in the group.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.

        1. The user would already be comfortable with the website layout and can easily click the banner message.

    2. As a Frequent User, I want to check to see if there are any new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link

    3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.
        1. At the bottom of every page their is a footer which content is consistent throughout all pages.
        2. To the right hand side of the footer the user can see "Subscribe to our Newsletter" and are prompted to Enter their email address.
        3. There is a "Submit" button to the right hand side of the input field which is located close to the field and can easily be distinguished.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   On some mobile devices the Hero Image pushes the size of screen out more than any of the other content on the page.
    -   A white gap can be seen to the right of the footer and navigation bar as a result.
-   On Microsoft Edge and Internet Explorer Browsers, all links in Navbar are pushed upwards when hovering over them.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/PhilipWilliams0/friday.com)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/PhilipWilliams0/friday.com
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/PhilipWilliams0/friday.com
> Cloning into 'friday.com'...
> remote: Enumerating objects: 287, done.
> remote: Counting objects: 100% (287/287), done.
> remote: Compressing objects: 100% (201/201), done.
> remote: Total 287 (delta 146), reused 206 (delta 67), pack-reused 0
> Receiving objects: 100% (287/287), 4.68 MiB | 5.25 MiB/s, done.
> Resolving deltas: 100% (146/146), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Create MongoDB database
My data was stored in a [MongoDB](https://cloud.mongodb.com/) collection set up using the following steps.
- Sign up / Sign In to mongodb and create a new cluster.
- Select 'collections' from the cluster dashboard.
- Click 'create database', and create database name and collection name.
- Click 'create collection' for any additional data collections needed for the app.

## Create Flask Application and install pymongo
In the terminal type the following commands to install the required packages:
    
- The following command will install the packages according to the configuration file
    ```
    $ pip3 install -r requirements.txt
    ```

Setup app
- Create `app.py` and `env.py` using the terminal
    ```
    touch app.py
    touch env.py
    ```

- Create gitignore file using the terminal to keep `env.py `from being pushed to github
    ```
    touch env.py
    ```

- Within the gitignore file add `env.py` and `__pycache__/`.
    ```
    env.py
    __pycache__/
    ```

Set up environment variables and flask instance
- Within `env.py` add the following environment variables:

    ```
    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "YOUR SECRET KEY")
    os.environ.setdefault("MONGO_URI", "YOUR MONGO URI")
    os.environ.setdefault("MONGO_DBNAME", "YOUR DATABASE NAME")
    ```

    - I used [randomkeygen]() to generate my secret key. 
    - To get your mongodb URI, go to your cluster dashboard and hit connect. Select your version of python and copy the string to the clipboard.

## Setting up the heroku app
In order to deploy the app via [heroku](https://dashboard.heroku.com/apps), the following steps must be taken. 

- In the terminal, create requirements.txt and Procfile for Heroku to run correctly
    ```
    pip3 freeze --local > requirements.txt
    ```
    ```
    echo web: python app.py > Procfile
    ```
- Push your files to gitHub
- Navigate to [heroku](https://heroku.com/) and create a new app in your dashboard.
- Assign an app name and region and hit 'create app'.
- In your dashboard, click to connect your gitHub and then locate the correct repository to be deployed.
- Click on the settings tab and then click 'reveal config vars' in order to input the data hidden in `env.py` as follows.
        
        IP                  0.0.0.0
        MONGO.DBNAME        friday-project
        MONGO_URI           MONGO URI copied from env.py
        PORT                5000
        SECRET_KEY          SECRET_KEY copied from env.py

- Click 'enable automatic deploy' in the app dashboard.
- Click view to see the deployed site!


## Credits

### Code

-   The full-screen hero image code idea came from [udemy](https://www.udemy.com/course/materialize-css-from-scratch-with-5-projects/)


### Content

-   All content was written by the developer with bulk of the CRUD structure used from Task Manager from Code institiute and adapted.

### Media

-   All Images were obtained from usplash. 

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

[Back to Contents](#contents)