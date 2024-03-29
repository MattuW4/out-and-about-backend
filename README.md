# **Out & About API (OAA API)**

## Table of Contents

- [Project](#project)
  * [Objective](#objective)
  * [Links to Deployed Project](#links-to-deployed-project)
- [Project Structure](#project-structure)
  * [Developer User Stories](#developer-user-stories)
- [Database Design](#database-design)
  * [Models](#models)
- [Features](#features)
- [Agile Workflow](#agile-workflow)
  * [Kanban Board](#kanbab-board)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# **Project**

## Objective

The Out & About app (referred to as OAA API in terms of the back end) is a social platform for sharing and promoting events locally and further afield with friends, family and other users. Whilst the app is intended for academic purposes, it is inspired by prospective user needs to connect on a smaller, organic scale and easily share events taking place that others within their social network would be interested in. A localised form of this kind of platform existed before larger players in the market created scaled offers that had greater scope than just being focused on connecting people within smaller social networks with a focus on purely promoting music or cultural events. However, the app could be scaled and is designed to accommodate high volumes of users with features that can be adapted to demand. 

The API also includes search and filter logic to improve user experience, and make it easier for users to find events tailored to their own interests. 

## Links to Deployed Project

  + Deployed project Heroku link: [Deployed Out & About API]( https://oaa-react-app-5abadda9e24d.herokuapp.com/)
  + Front end GitHub repo: [Out & About Front End](https://github.com/MattuW4/out-and-about-frontend)

## Project Structure

The overall structure of the project was modelled on the [drf-api](https://github.com/Code-Institute-Solutions/drf-api) walkthrough as a basis to build on. Custom models have been developed where possible including events, attending, contacts, reviews and subscribers. 

## Developer User Stories
This project was developed with using epics as the basis to organise a number of developer goals and user stories were created, each one given a prioritisation using the MoSCoW method. These epics included
+ Profile page (As a site user I can interact with my profile and other profiles so that I develop social connections and can access information.)
+ Events page (As a site user I can update an event so that it is the most current listing.)
+ Events page (As a site user I can find out more information on an event so that I keep up to date with the event.)
+ Attending events (As a site user I can interact with events so that I can stay updated with news and information or show support for an event.)
+ Adding events (As a logged in user I can create events so that I can promote events I am involved in or support.)
+ Authentication (As a site user I can register and log in/out so that I am able to securely access different parts of the site and safely create, request and update data.)
+ Navigation (As a site user I can access features so that I can navigate and interact with the site.)
+ Reviews & Contact (As a user I can create reviews and contact the site administrator so that I can leave feedback for other users and the site admin.)
+ Full stack technologies (As a site user I can use front and back end technologies so that I am able to interact with the site and have full CRUD of data.)

The user stories below indicate the grouping of epics linked to an area as well as API endpoints associated with the tasks.

### Profiles (Epic: Profile Page/Authentication/Navigation/Full stack technologies Endpoints: profiles/ profiles/:id)

+ As a developer I can view a list of all profiles so that I can see all profiles created
+ As a developer I can view the details of a profile so that I can see individual profile data
+ As a developer I can edit a profile when logged in so that I can update my personal information
+ As a developer I can delete a profile I own so that I can remove user date from the API

### Events (Epics: Event Page/Events page/Attending events/Adding events/ Authentication/Navigation/Full stack technologies Endpoints: events/ events/:id)

+ As a developer I can view a list of all events so that I can see all events 
+ As a developer I can view an event so that I can see the event details
+ As a developer I can create a new event so that the event appears in the events list
+ As a developer I can edit an event I created so that I can update event information
+ As a developer I can delete an event I created so that I can remove the data from the API

### Comments (Epics: Attending events Authentication/Navigation/Full stack technologies Endpoints: comments/ comments/:id)

+ As a developer I can create a comment so that it is linked to an event
+ As a developer I can view a list of all comments so that I can see all comments the API
+ As a developer I can retrieve a single comment by ID so that I can edit or delete the comment
+ As a developer I can edit a comment I created so that I can update the comment information
+ As a developer I can delete a comment I created so that I can remove the data from the API

### Attending (Epics: Attending events Authentication/Full stack technologies Endpoints: attending/ attending/:id)

+ As a developer I can create an attending object linked to a single event so that I can show attendance to the event
+ As a developer I can delete an attending object I created so that I can remove the date from the API
+ As a developer I cannot delete an attending object that another user created
+ As a developer I can view a list of all the attending objects so that I can see all created in the API

### Subscribers (Epics: Attending events/profile page/Authentication/Full stack technologies Endpoints: subscribers/ subscribers/:id)

+ As a developer I can create a subscription so that I can subscribe to another user
+ As a developer I can view a list of subscribers so that I can see all the subscriptions created
+ As a developer I can delete a subscription so that I can unsubscribe from another user 

### Reviews subscribers (Epics: Reviews & Contacts/Authentication/Full stack technologies Endpoints: reviews/ reviews/:id)

+ As a developer I can create a review so that I can link a review and rating to an event
+ As a developer I can view a list of all reviews so that I can see all of the reviews created in the API
+ As a developer I can edit a review I created so that I can update the review information
+ As a developer I can delete a review I created so that I can remove data from the API

### Contact (Epics: Reviews & Contacts/Authentication/Full stack technologies Endpoints: contacts/ contacts /:id)

+ As a developer I can create a contact message so that I can contact the site admin
+ As a developer I can view a list contact messages created so that I can see all contacts in the API

### Search and Filter

+ As a developer I can access a search field in the events list so that I can search for an event
+ As a developer I can filter events by category so that I can only see events relating to a specific category
+ As a developer I can filter events by profiles I subscribe to so that I can see events relating to profiles I am interested in
+ As a developer I can view a list of profiles subscribed to by another profile so that I can see which profiles are subscribing to it
+ As a developer I can view a list of events I have posted and am attending by ID so that I can see only events I am interested in attending
+ As a developer I can view a list of events relating to a profile so that I can only see events posted by a single user
+ As a developer I can view a list of comments linked to an event so that I can view comments relating to a specific event id
+ As a developer I can view a list of reviews linked to an event so that I can see the reviews relating to a specific event id

# Database Designs

## Models

The following are models developed as part of the OAA API:
 * User (Established automatically when a user is created)
 * Profile (Established automatically when a user is created)
 * Event (A posting to publicise an event)
 * Comment (A user can leave a comment on any event)
 * Attending (A user can indicate if they intend to attend an event or not)
 * Subscribe (Users can subscribe to other event organisers or users)
 * Review (Users who have attended a past event can leave a review)
 * Contact (A user can contact the site admin with feedback)

The following Entity Relationship Diagram demonstrates relationships between the models:
![ERD]( https://res.cloudinary.com/deoxxigyw/image/upload/v1711662980/ERD_hrd05r.png)

# Features

## Homepage

When you first enter the API site, you are directed to a homepage, with welcome message

## Profile Data

A user can view a list of all profiles in the API within the Profile List section. The create a profile process is completed automatically through the user registration process. 

## Events Data

Within the Events List section, a user can view a list of all events in the API. When logged in, if the user views the details of a single event which they created Update and Delete functionality are available. A pre-populated form is available to edit the event. A delete button is available to delete the event from the API.

## Comments Data

A user can view a list of all comments in the API within the comments list section. When logged in, a form is available under the comments list to create a new comment. The event to comment on can be selected from the dropdown. Additional Update and Delete functionality is available when logged in. A pre-populated form is available to edit the comment. A delete button is available to delete the comment.

## Attending

A user can view a list of all interested events in the API within the Attending List section. When logged in a form is available to create a new interested object. The event a user wants to attend can be selected from the dropdown. If a user tries to attend the same event twice, they see an error message. A logged in user can delete an attend object to un-attend an event

## Subscribers Data

A user can view a list of all subscriber events in the API from the subscribers list. When logged in, a user can create a new subscribing object. The user they want to subscribe to can be selected from the dropdown, to link the subscriber object with another user profile. A user can delete a subscribing object to unsubscribe from a profile.

## Reviews Data

A user can view a list of all reviews in the API within the Review List section. When logged in a user can create a new review. The event they want to review can be selected from the dropdown, and a review text and rating must be entered to review successfully. If a user tries to review same event twice, they see an error message. A logged in user can edit or delete a review that they have created as well as seeing other user reviews of an event they have attended.

## Contact Data

A user can view a list of all contacts submitted in the API within the Contact List section. A logged in user can create a new contact. 

# Agile Workflow

## Kanban Board

The GitHub Kanban board was used to build the [OAA API project](https://github.com/users/MattuW4/projects/6) using Agile principles from the start. User stories were created for a developer to follow and test during the build process. Individual sprints were undertaken for the project to achieve developer uer stories. 

The MoSCoW method was employed for each user story to provide a level of prioritisation. 

# Testing

Click [**_here_**](TESTING.md) for the OAA testing documentation.

# Technologies Used

## Languages

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) – language used to develop the OAA API backend

## Frameworks & Software

* [Django Rest Framework (DRF)](https://www.django-rest-framework.org/) – API development framework
* [PEP8 Code Institute Linter]( https://pep8ci.herokuapp.com/) - tool to check Python code for style conventions in PEP 8.
* [Github](https://github.com/) - hosts the back end repository and project board. Git used for version control.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - cloud platform application deployed to.
* [Cloudinary](https://cloudinary.com/) – cloud service for hosting image files.

## Libraries

The libraries used in this project are located in the requirements.txt file and have been documented below

* [asgiref](https://pypi.org/project/asgiref/) – The Asynchronous Server Gateway Interface is a calling convention for web servers to forward requests to asynchronous-capable Python programming language frameworks, and applications.
* [cloudinary](https://pypi.org/project/cloudinary/) - provides cloud-based image and video management services. It enables users to upload, store, manage, manipulate, and deliver images and video for websites and apps
* [coverage]( https://coverage.readthedocs.io/en/latest/) - tool is used to estimate the test coverage that a test suite under development affords to implementations of its related API specification.
* [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) - This simple Django utility allows utilisation of the 12factor inspired DATABASE_URL environment variable to configure a Django application.
* [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - Drop-in API endpoints for handling authentication securely in Django Rest Framework. 
* [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
* [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
* [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
* [django-cors-headers](https://pypi.org/project/django-cors-headers/) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
* [django-filter](https://pypi.org/project/django-filter/) - Django-filter is a reusable Django application allowing users to declaratively add dynamic QuerySet filtering from URL parameters.
* [django-rest-framework](https://pypi.org/project/djangorestframework/) - web-browsable Web APIs.
* [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework.
* [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
* [oauthlib](https://pypi.org/project/oauthlib/) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
* [Pillow](https://pypi.org/project/Pillow/8.2.0/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
* [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
* [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation of RFC 7519.
* [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support for modern servers and consumers.
* [pytz](https://pypi.org/project/pytz/) - This is a set of Python packages to support use of the OpenID decentralized identity system in your application, update to Python 3
* [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - P    rovides first-class OAuth library support for Requests.
* [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

# Deployment

The project was deployed to [Heroku](https://www.heroku.com). Follow the steps below to deploy.

# # Repository

1.Create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then selecting 'Use this template'.

2. Fill in details for new repository and click 'Create Repository From Template'.

3. Click on the 'Gitpod' button to open a workspace.

4. Install Django and supporting libraries (gunicorn, 'dj_database_url psycopg2, 'dj3-cloudinary-storage)

5. Create  requirements.txt file (pip3 freeze --local > requirements.txt)

6. Create the project (django-admin startproject YOUR_PROJECT_NAME ) 

7. Next create the applications (using python3 manage.py startapp APP_NAME)

8. Add applications to settings.py in the INSTALLED_APPS list.

8. Migrate models to database using the following steps:
* ```python3 manage.py makemigrations –dry-run``` 
* ```python3 manage.py makemigrations``` 
* ```python3 manage.py migrate``` 
* ```python3 manage.py runserver``` 
## Heroku
9. Create an application on Heroku, attach a database, prepare environment and settings.py file and setup Cloudinary storage for static and media files.

* Sign into [Heroku](https://www.heroku.com/) account, click 'New' to create a new app. 

10. Choose a app name, choose region and click 'Create app".

## ElephantSQL
11. Next we need to connect the PostgreSQL database to the app from [ElephantSQL](https://customer.elephantsql.com/login).  Log in to the ElephantSQL dashboard and click 'Create New Instance' to create a new database. Return to the ElephantSQL Dashboard, and click into your new database instance. Copy the Database URL and head back to Heroku.

## Backend setup

12. In Heroku app settings, click 'Reveal Config Vars' button. Add DATABASE_URL config var and paste in the URL from ElephantSQL. 

13. In GitPod create a new env.py in the top level directory. Then add:
* ```import os``` 
* ```os.environ["DATABASE_URL"]``` 
* ```os.environ["SECRET_KEY"]``` 

14. In Heroku Config Vars settings, create SECRET_KEY config var and copy secret key from the env.py file. Add env.py file into.gitignore file.

15. To connect to the environment and settings.py file add the following code:

```import os```

```import dj_database_url```

```if os.path.isfile("env.py"):```

```import env```

16. In the settings file, remove the insecure secret key and replace it with:
```SECRET_KEY = os.environ.get('SECRET_KEY')```

17. Comment out old database settings in the settings.py file to replace with the postgres database instead of the sqlite3.

Add the link to the DATABASE_URL that from environment file.

18. Save all fields and migrate.

```python3 manage.py migrate```

## Cloudinary setup

19. Set up [Cloudinary]( https://cloudinary.com/). Create Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

20. In env.py file in Gitpod add the Cloudinary url):

```os.environ["CLOUDINARY_URL"] = "cloudinary://************************"```

21. In Heroku add the Cloudinary url to Config Vars. Also add disable collectstatic var.

22. In settings.py file add Cloudinary Libraries installed earlier to the INSTALLED_APPS. Ensure correct order.

* cloudinary_storage
* django.contrib.staticfiles
* cloudinary

23. For Django to use store static files extra rows settings.py are required.

24.  Add Heroku app and localhost to the ALLOWED_HOSTS list:

```ALLOWED_HOSTS = ['APP_NAME.herokuapp.com', 'localhost']```

25. Create standard file directory in Gitpod.

* Create **Procfile* and add ```web: gunicorn PROJ_NAME.wsgi?```.

26. Using git version control commit and push to Github by.

* ```git add .```
* ```git commit -m "Initial deployment Commit```
* ```git push```

27. To deploy in Heroku click the 'Deploy' tab. For method, select 'Github'. Search for your repository to deploy and click connect.

28. Select manual deployment section and click 'Deploy Branch'. 

## Forking the repository

1. Login/create [GitHub]( https://github.com/) account

2. Navigate to desired repository to clone

3.In top right click ‘Fork’

4. Adjust form fields where required then click ‘Create Fork’ 

## Cloning and local setup

To clone and set up this project you need to follow the steps below.

1. Login/create [GitHub]( https://github.com/) account and navigate to desired repository

2. Click on the 'code' menu and ensure ‘HTTPS’ selected. Click on the clipboard icon to copy the URL.

3. Using an IDE and open Git Bash to create a new project. 

4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.

# Credits

* The default profile image was provided by Code Institute but edited to fit the aesthetic of the events site
* The placeholder image upload picture was taken from [UXWing]( https://uxwing.com/upload-image-icon/)
* Tutorial video on [YouTube](https://www.youtube.com/watch?v=D3iPIoTL9skhttps://codingpr.com/star-rating-blog/) to learn about implementing a rating system 
* [Django tutorial](https://django.fun/qa/16172/) to understand average star rating system
* The Code Institute's DRF walkthrough with Readme and Testing file formatting informed by fellow student backend repositories


