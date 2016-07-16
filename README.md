# EVE-Monitor

- Originally cloned from [here](https://github.com/flesser/django-crest-example)
- made private for CCP's CREST [API competition](https://www.reddit.com/r/Eve/comments/45wpx5/dev_blog_the_eve_online_api_challenge_ccp_foxfour/?ref=share&ref_source=link) from Reddit

This is a simple Django App with EVE Online Single Sign-On (SSO) and authenticated CREST access.
It depends on [Python Social Auth](http://psa.matiasaguirre.net/) to integrate EVE SSO with Django's builtin user authentication system and uses [PyCrest](https://forums.eveonline.com/default.aspx?g=posts&t=398676) to interact with the CREST API.

## Live Demo
A live demo is available[here](http://evecrest.herokuapp.com/login/)

## Getting started
If you want to try it out on your own, loosely follow these steps +/- some python package fun:

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
  - as *Callback URL* use `http://your-server.com/complete/eveonline/` (or `http://localhost:8000/complete/eveonline/` for the Django development server)

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
8. ???
9. Profit!

~~## How to Use~~

~~To use this project, you need an api key from your account:~~

~~1. Generate an API key/token to use on the site from your account [API keys](https://community.eveonline.com/support/api-key/)~~
~~2. Allow full access for full featured usage (everything should be highlighted in yellow)~~
~~3. Sign into the SSO link for personalize usage (you are redirected back and are authed)~~


## info/sources/docs

- [EVE Online](https://eveonline.com/)
- [EVE 3rd party dev - read the docs](https://eveonline-third-party-documentation.readthedocs.org)
- [CCP dev resources via CCP](https://developers.eveonline.com/resource/resources)
- [CCP DevBlog](https://developers.eveonline.com/blog)
- [CCP DevBlog - crest features](https://developers.eveonline.com/blog/article/the-eve-online-api-challenge)
- [Pycrest - python api wrapper](https://pycrest.readthedocs.org)
- [XML api docs](http://wiki.eveuniversity.org/EVE_API_Guide)
- [XML api endpoints](http://ned.karbowiak.dk/API)
- [RESTful CREST YT vid](https://www.youtube.com/watch?v=QMQOjUjrZIo)
- [CREST CCP presentation - intro to REST/OAuth](http://bambuser.com/v/2494220)

~~- [in-game browser specs](http://wiki.eveuniversity.org/In_Game_Browser_Development)~~ DEPRECATED


- [CREST js - has endpoints/schema](http://jimpurbrick.com/crestmatic/)
- [really old images, etc](https://community.eveonline.com/news/dev-blogs/eve-data-export-rmr-edition/)
- [~29mil killmails](https://www.reddit.com/r/evetech/comments/3ohd1v/28285480_killmails_crest/)
- [python cron job - zkill](https://www.reddit.com/r/evetech/comments/4c2xgy/lf_kills_feed/d1fx8z7)
- [ridetheclown - full api results as of Odyssey](http://ridetheclown.com/eveapi/audit.php)

## CCP Copyright Notice [Here](https://developers.eveonline.com/resource/license-agreement)

EVE Online and the EVE logo are the registered trademarks of CCP hf. All rights are reserved worldwide. All other trademarks are the property of their respective owners. EVE Online, the EVE logo, EVE and all associated logos and designs are the intellectual property of CCP hf. All artwork, screenshots, characters, vehicles, storylines, world facts or other recognizable features of the intellectual property relating to these trademarks are likewise the intellectual property of CCP hf. CCP hf. has granted permission to evepaste to use EVE Online and all associated logos and designs for promotional and information purposes on its website but does not endorse, and is not in any way affiliated with, evepaste. CCP is in no way responsible for the content on or functioning of this website, nor can it be liable for any damage arising from the use of this website.




Oh you want to deploy it somewhere? I've used heroku in my example, so:


## Deoloy with Heroku Toolbelt

set config vars on heroku to match env vars locally + postgres add-on

you can always test if heroku will work with `heroku local`

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

5. ???
6. profit

(or just register the heroku app and connect GH account, push to GH master)
