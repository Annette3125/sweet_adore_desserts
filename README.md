![Sweet adore desserts logo](docs/static/desserts_logo_for_readme.jpg) ![Sweet adore desserts logo2](docs/static/main_logo_for_readme.jpg)

# Sweet Adore Desserts


## Welcome to Rugile's Desserts!


### Delicious inspiring collection!


#### Create virtual environment in the project root directory:
```
$ python3.12 -m venv venv
```

## Activate the virtual environment:
- For Linux / Mac:

```
$ source venv/bin/activate
```

- For Windows 

```
$ .\venv\Scripts\activate
```

### Install the required packages:

```
(venv) $ pip install -r requirements.txt
```


[1] Prepare the database:

```
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
```


#### Credentials for the existing superuser in the database:
User admin has to enter e-mail to sign in:
- E_mail: anetuks@gmail.com
- Password: labas

If you would like to use the existing database,
you can optionally create your own superuser:

```
(venv) $ python manage.py createsuperuser
```

#### Credentials for the existing staff user:
- Username it is e-mail: `r.velaviciute@gmail.com`
- Password: `tortas123`
The password for all other users (clients) in the database is `tortas123`.

# Running
### [1] Set the environment variables:


Finally, run the development server:

```
(venv) $ python manage.py runserver
```

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
[requirements.txt](https://github.com/Annette3125/sweet_adore_desserts/blob/main/requirements.txt).

### Latest releases

**v0.1.0** (2025-01-01)


### API references

None

### [Licence](https://github.com/Annette3125/sweet_adore_desserts/blob/main/LICENCE)

The MIT License (MIT)

Copyright (c) 2025 