
# TODOS APPS

This project was created with two well-known frameworks, namely Django Rest Framework as a Back-End Application and Vue+Vuetify 3 as a Front-End Application. The purpose of this project is only as a means to learn to use these two frameworks so that you are familiar with how DRF and Vue work.

# How to run this project?

You can run this project in a local environment and make sure you have npm and python installed.

For FE, you can open a terminal and type the following command:
```
cd fe
npm install
npm run serve
```

For BE, you can run the project with the following command:
```
cd be
python -m venv env
env\scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Notes

Before you run the BE project, make sure you have restored the database PostgreSQL provided in the repository. The backup file is in the 'be' folder with the name todos.sql (You can restore the database using various methods, in my case, I used the pgAdmin application).

After you restore the database file, make sure you adjust the API settings according to the database configuration you are using.

You can set the API database config in the be/todoapps/setting.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todos',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

After that, you can set NAME, USER, HOST, PASSWORD, and USER according to the configuration you have done.