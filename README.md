# recipe-app-api

[![Build Status](https://travis-ci.org/profmcdan/recipe-app-api.svg?branch=master)](https://travis-ci.org/profmcdan/recipe-app-api.svg?branch=master)

--
Recipe App api

## commands

RUN `docker build .`

RUN `docker-compose build`

RUN `docker-compose run app sh -c "django-admin.py startproject app"`

RUN `docker-compose run app sh -c "python manage.py test"`

RUN `docker-compose run app sh -c "python manage.py startapp core"`

RUN `docker-compose run app sh -c "python manage.py makemigrations core"`

RUN `docker-compose run app sh -c "python manage.py migrate"`

RUN `docker-compose up`
