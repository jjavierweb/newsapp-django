## Welcome to the NewsApp

This is an app that contains Authentication and Authorization

The app is using postgre with a docker container using docker compose

### Docker DB
install Docker compose and run the command below to create the container

    docker-compose -f scripts/dev_env.yaml up -d 
  
### Recommendations:
It's recommended to use a development environment for this app with PIPENV or virtualenv
To do so, follow this steps:

    python --version
    pip3 install pipenv
    cd /dev_folder/
    pipenv install
    pipenv shell
    pip install -r requirements.txt

After doing those steps your environment should be ready to go, all you need to do then is to create the migrations and the superuser and run the application

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser # this will provide you some prompts
    python manage.py runserver

After running the server then all you need to do is click on the link that the last command provides and from there you can create your users and articles

### Email cofiguration:
For the email configuration all you need to do is go to the 
<strong>
newspaper_project/settings.py
</strong> 
and change the entries

    EMAIL_HOST = 'your.service.provider.server'
    EMAIL_HOST_USER = 'email.username'
    EMAIL_HOST_PASSWORD = 'email.username.password'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True # change to false if your provider does not use TLS
    DEFAULT_FROM_EMAIL = '' # this could be empty or not depending on your provider

