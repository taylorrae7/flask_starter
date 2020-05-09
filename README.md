## Flask Start-Up! 

Starter app for a flask application

Key Features/Packages being used: 
* Modular Flask application architecture using [Application Factories][app-factory] and [Blueprints][blueprints]
* Database migrations support ([Flask-Migrate][flask-Migrate] and [Alembic][alembic])
* ORM integration ([Flask-SQLAlchemy][flask-sqlachemy]) and ([SQLAlchemy][sqlalchemy])
* Handling Forms ([Wtforms][wtforms])
* Secure user authentication with password hashing ([Flask-Login][flask-login] and [Flask-Bcrypt][flask-bcrypt])

## Table of contents
* [Setup](#setup)
* [Quickstart](#quickstart)
    * [Project Setup](#project-setup) 
    * [Database Setup](#databse-setup)
    * [Run](#run)
* [File Structure](#file-structure) 
* [Heroku](#heroku)


### Setup

Make sure you have the following downloaded on your machine. 

* Python 3.7
* PostgreSQL (preferably V.12)

Recommended 
* pgAdmin 4 (Postgres Management Tool is great if uncomfortable with CLI)
* PyCharm PE (it's free for students) or any IDE you are comfortable with.



### Quickstart

#### Project Setup

1. Clone the repo
2. Navigate to the directory and add to personal git

    ```
    git remote rm origin
    git remote add origin <the location of my new git repository>
    git push -u origin master
    ```

3. Create virtual environment 
4. Install dependencies
```
pip install -r requirements.txt 
```

#### Database Setup

1. Create new PostgreSql database 
2. Open config.py and update SQLALCHEMY_DATABASE_URI to the name of database created in step 1.
3. Delete the migrations folder
4. Initialize the database by running the following: 
```
python run.py db init
python run.py db migrate
python run.py db upgrade
```

the database should be all set up now. 

#### Run
```
python run.py runserver
```



### File Structure
The high level overview of the project file structure 
``` 
.
│
├─ app/                             # All application code in this directory.
│  │
│  ├─ forms/                        # Stores all of the form templates, seperated by blueprint
│  │
│  ├─ static/                       # Base styling and images.
│  │
│  ├─ templates/                    # HTML templates 
│  │  ├─ errors/                    # All error pages templates
│  │  ├─ layouts/                   # Base layouts for the app 
│  │  │  ├─ _base.py                # Layout for logged in users - full navbar                 
│  │  │  └─ _auth_base.py           # Layout for login/register - limited navbar 
│  │  │
│  │  └─ pages/                     # All of the main pages are here - as the app grows break this into folders. 
│  │
│  ├─ views/                        # Contains all of the routes 
│  │  ├─ auth.py                    # Holds all routes pertaining to user authentication (login, register,logout)
│  │  └─ home.py                    # Holds all routes pertaining to base application (home and about pages) 
│  │
│  ├─ __init__.py                   # Flask create_app() factory.
│  └─ models.py                     # Stores all of the database models for the project
│
├─ migrations/                      # Stores previous database changes
│  └─ versions/                     # Migrations upgrade/downgrade for each version of database
│
├─ tests/                           # Tests are structured similar to the application.
│
├─ config.py                        # All configs for the app
└─ manage.py                        # Main entry-point into the Flask application.

```

### Heroku

1. Create a heroku account and create a new app.
 
2. Click on the Resources tab and 
    * Search Heroku Postgres. 
    * Add Hobby Dev - Free version to your app. 
    
3. Click on Deploy
    * Scroll down to Deployment method and click on Github
    * Connect to this projects github repository 
    * select the branch you want connected and enable automatic deploys.
    
4. Push changes to github and the project will begin to build. 

5. After the code is pushed migrate the local database to the postgres database by running 
```
heroku run python run.py db upgrade --app heroku-app-name
```

6. The app is now running on heroku. 


[alembic]: http://alembic.readthedocs.org/en/latest/
[app-factory]: http://flask.pocoo.org/docs/patterns/appfactories/
[blueprints]: http://flask.pocoo.org/docs/blueprints/
[flask-bcrypt]: https://pythonhosted.org/Flask-Bcrypt/
[flask-login]: https://flask-login.readthedocs.org/en/latest/
[flask-migrate]: http://flask-migrate.readthedocs.org/en/latest/
[flask-script]: http://flask-script.readthedocs.org/en/latest/
[sqlalchemy]: https://docs.sqlalchemy.org/en/13/orm/
[flask-sqlalchemy]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
[wtforms]: https://wtforms.readthedocs.io/en/stable/

