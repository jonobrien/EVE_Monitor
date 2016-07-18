# EVE-Monitor

This is a simple Django App with EVE Online Single Sign-On (SSO) and authenticated CREST access. It shows some basic data that can be acquired via both the authed and public CREST API.
It uses [Python Social Auth](http://psa.matiasaguirre.net/) to integrate EVE SSO with Django's builtin user authentication and uses [PyCrest](https://github.com/jonobrien/PyCrest) to interact with the CREST API.

## Live Demo
A live demo is available [here](http://evecrest.herokuapp.com/login/)

## Getting started
If you want to try it out on your own, loosely follow these steps:

1. Get the code:
  ```bash
  $ git clone https://github.com/jonobrien/eve_crest.git
  ```

2. Install dependencies
  ```bash
  $ pip install -r requirements.txt
  ```

3. Register a new application on [here](https://developers.eveonline.com/applications/)
  - for *Connection Type* select **CREST Access**
  - in *Permissions* add **publicData** and all `character*` to the Requested Scopes List (see settings.py)
  - as *Callback URL* use `http://<your-server.com>/complete/eveonline/` (or `http://localhost:8000/complete/eveonline/` for the Django development server)

4. edit env vars and enter your application's Client ID and Secret Key:
  ```bash
  EVE_DEV_ID='<Your EVE CREST Application Key>'
  EVE_DEV_SECRET='<Your EVE CREST Application Secret>'
  LOCALDB='<something>'
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


## info/sources/docs

- [EVE Online](https://eveonline.com/)
- [EVE 3rd party dev - read the docs](https://eveonline-third-party-documentation.readthedocs.org)
- [CCP dev resources](https://developers.eveonline.com/resource/resources)
- [CCP DevBlog](https://developers.eveonline.com/blog)
- [CCP DevBlog - crest features](https://developers.eveonline.com/blog/article/the-eve-online-api-challenge)
- [XML api docs](http://wiki.eveuniversity.org/EVE_API_Guide)
- [XML api endpoints](http://ned.karbowiak.dk/API)
- [RESTful CREST YT vid](https://www.youtube.com/watch?v=QMQOjUjrZIo)
- [CREST CCP presentation - intro to REST/OAuth](http://bambuser.com/v/2494220)


- [CREST js - has endpoints/schema](http://jimpurbrick.com/crestmatic/)
- [really old images, etc](https://community.eveonline.com/news/dev-blogs/eve-data-export-rmr-edition/)
- [~29mil killmails](https://www.reddit.com/r/evetech/comments/3ohd1v/28285480_killmails_crest/)
- [python cron job - zkill](https://www.reddit.com/r/evetech/comments/4c2xgy/lf_kills_feed/d1fx8z7)
- [ridetheclown - full api results as of Odyssey](http://ridetheclown.com/eveapi/audit.php)


- cloned [here](https://github.com/flesser/django-crest-example)
- made private for CCP's CREST [API competition](https://www.reddit.com/r/Eve/comments/45wpx5/dev_blog_the_eve_online_api_challenge_ccp_foxfour/?ref=share&ref_source=link) from Reddit

----

### CCP Copyright Notice [Here](https://developers.eveonline.com/resource/license-agreement)

----


## Deploy with Heroku Toolbelt

set config vars on heroku to match env vars locally + postgres add-on

1. clone repo
2. add heroku remote

  ```bash
  $ heroku git:remote -a <appname>
  ```

3. make an edit and commit to heroku master

  ```bash
  $ git push heroku python3:master
  ```

4. tell postgres to migrate (heroku doesn't run this command by default)

  ```bash
  $ heroku run python manage.py migrate
  ```
