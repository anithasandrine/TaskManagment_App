# Getting Started with the task management app

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/anithasandrine/TaskManagment_App.git
    $ cd TaskManagment_App
    

create virtualenv for project.
    $ python -m venv virtualenv_name

Activate the virtualenv for your project.
    $ venv\Scripts\activate

    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

open this link in your browser:

    $ http://127.0.0.1:8000/