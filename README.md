# EVE-CRESTFUL

- Originally cloned from [here](https://github.com/flesser/django-crest-example)
- made private for CCP's CREST [API competition](https://www.reddit.com/r/Eve/comments/45wpx5/dev_blog_the_eve_online_api_challenge_ccp_foxfour/?ref=share&ref_source=link) from Reddit

This is a simple Django App with EVE Online Single Sign-On (SSO) and authenticated CREST access.
It depends on [Python Social Auth](http://psa.matiasaguirre.net/) to integrate EVE SSO with Django's builtin user authentication system and uses [PyCrest](https://forums.eveonline.com/default.aspx?g=posts&t=398676) to interact with the CREST API.

## Live Demo
A live demo used to be available[here](http://django-crest-example.dubiose-briefkastenfirma.de/) but it no longer works due to db issues and changes to the CREST api

## Getting started
If you want to try it out on your own, loosely follow these steps +/- some python package fun:

1. Get the code:
  ```bash
  $ git clone https://github.com/jonobrien/eve_crest.git
  ```

2. Install dependencies (mainly [PyCrest](https://github.com/jonobrien/PyCrest) and [Python Social Auth](https://github.com/omab/python-social-auth) with Python3.4):
  ```bash
  $ pip install -r requirements.txt
  ```

3. Register a new application on https://developers.eveonline.com/applications
  - choose name and description as you like
  - for *Connection Type* select **CREST Access**
  - in *Permissions* add **publicData** to the Requested Scopes List
  - as *Callback URL* use `http://your-server.com/complete/eveonline/` (or `http://localhost:8000/complete/eveonline/` for the Django development server)

4. edit `.bashrc` and enter your application's Client ID and Secret Key:
  ```bash
  EVE_DEV_ID='<Your EVE CREST Application Key>'
  EVE_DEV_SECRET='<Your EVE CREST Application Secret>'
  ```

5. initialize the database:
  ```bash
  python manage.py migrate
  ```

6. run development server:
  ```bash
  python manage.py runserver
  ```

7. point your browser to [http://localhost:8000/](http://localhost:8000/)

8. ???

9. Profit!

## Deoloy with Heroku

1. clone repo

2. add heroku remote

```bash
$ heroku git:remote -a <appname>
```

3. make an edit and commit to heroku master

```bash
$ git push heroku python3:master
```

4. tell postgres to migrate

```bash
$ heroku run python manage.py migrate
```

4. ???

5. profit
