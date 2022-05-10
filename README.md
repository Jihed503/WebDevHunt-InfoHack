# WebDevHunt-InfoHack
-----

WebDevHunt is hiring website that fasciliate the discovery of new talents and the communication between employer and potential employees.

### Tech Stack

Our tech stack includes:

* **Sqlite3** as our database of choice
* **Python3** and **Django** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with Bootstrap 4 for our website's frontend

### Main Files: Project Structure

  ```sh
├── db.sqlite3
├── manage.py
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   └── devregister.css
│   └── js
│       ├── confirm.js
│       └── forgotpwd.js
├── templates
│   ├── clientsignup.html
│   ├── developer.html
│   ├── devsignup.html
│   ├── home.html
│   ├── login.html
│   ├── new_reply.html
│   └── project.html
├── webdevhunter
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc (deleted)
│   │   ├── settings.cpython-39.pyc (deleted)
│   │   ├── urls.cpython-39.pyc (deleted)
│   │   └── wsgi.cpython-39.pyc (deleted)
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── webdevhunterapp
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc (deleted)
    │   ├── admin.cpython-39.pyc (deleted)
    │   ├── apps.cpython-39.pyc (deleted)
    │   ├── models.cpython-39.pyc (deleted)
    │   └── views.cpython-39.pyc (deleted)
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_remove_technologie_developers_developer_technologies.py
    │   ├── 0003_developer_about.py
    │   ├── 0004_developer_image.py
    │   ├── 0005_project_name.py
    │   ├── 0006_project_image.py
    │   ├── 0007_project_github.py
    │   ├── 0008_alter_reply_rating.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-39.pyc
    │       ├── 0002_remove_technologie_developers_developer_technologies.cpython-39.pyc
    │       ├── 0003_developer_about.cpython-39.pyc
    │       ├── 0004_developer_image.cpython-39.pyc
    │       ├── 0005_project_name.cpython-39.pyc
    │       ├── 0006_project_image.cpython-39.pyc
    │       ├── 0007_project_github.cpython-39.pyc
    │       ├── 0008_alter_reply_rating.cpython-39.pyc
    │       └── __init__.cpython-39.pyc
    ├── models.py
    ├── tests.py
    └── views.py
```

Overall:
* Models are located in `webdevhunterapp/models.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.

### Development Setup

First, [install Django](https://www.djangoproject.com) if you haven't already.

  ```
  $ cd ~
  $ pip install Django==4.0.4
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ python manage.py runserver
  ```

4. Navigate to Home page [http://localhost:8000](http://localhost:8000)
