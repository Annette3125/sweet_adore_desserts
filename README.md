![Sweet adore desserts logo](docs/static/desserts_logo_for_readme.jpg) ![Sweet adore desserts logo2](docs/static/main_logo_for_readme.jpg)

# Sweet Adore Desserts


## Welcome to Rugile's Desserts!

##### Delicious inspiring collection!


### Installation


#### Create virtual environment in the project root directory:
```
$ python3.12 -m venv venv
```

#### Activate the virtual environment:
- For Linux / Mac:

```
$ source venv/bin/activate
```

- For Windows 

```
$ .\venv\Scripts\activate
```

#### Install the required packages:

```
(venv) $ pip install -r requirements.txt
```

### Running

##### [1] Set the environment variables:

Create a `.env` file in the project's root directory and add
environment variables to this file.

Example `.env` file:

```
DEBUG=True
SECRET_KEY=django-insecure-_aanv3ucg@3s8=v0)qzto+00i#v8e6w1(8!i3kr-n8_x28v-t^
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://username:password@localhost:5432/dbname
STATIC_ROOT=
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=name@gmail.com
EMAIL_USE_TLS=True
EMAIL_HOST_PASSWORD=oiintrsytlvjtuta
UNSPLASH_API_KEY=_23r28kZ-Tkjt_rpyTuT0QRfuiZqkxgJU0wDw9ZYcYs
```
See also: [.env.example](.env.example)

##### [2] Prepare the database:
Add your database credentials to the .env file, using DATABASE_URL variable.

```
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
```

Create your own superuser:

```
(venv) $ python manage.py createsuperuser
```


#### [3] Run development server:

```
(venv) $ python manage.py runserver
```

### Software dependencies

[Django](https://docs.djangoproject.com/en/5.1/) – 
the web framework for perfectionists 
with deadlines. Django aims to follow Python’s 
["batteries included" philosophy](https://docs.python.org/3/tutorial/stdlib.html#tut-batteries-included). 
It ships with a variety of extra, optional tools that solve 
common web development problems.

[Bootsrap v5.3](https://getbootstrap.com/) - 
powerful, extensible, and feature-packed frontend toolkit.

[Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) -  
forms have never been this crispy.

[TinyMCE](https://www.tiny.cloud/) - adds a fully-featured, sleek and intuitive 
rich text editor to our app – in just a few lines of code.

[Django-environ](https://pypi.org/project/django-environ/) 
- it reads key-value pairs from 
a .env file and can set them as environment variables.
It helps in the development of applications following the 
[12-factor](https://12factor.net/)
For the full list of software dependencies see 
[requirements.txt](requirements.txt).

### Latest releases

**v1.0.0** (2025-04-10)


### API references

None

### [Licence](https://github.com/Annette3125/sweet_adore_desserts/blob/main/LICENCE)

The MIT License (MIT)

Copyright (c) 2025 