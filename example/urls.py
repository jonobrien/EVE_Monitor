from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from example.crest_app.views.home import HomeView
from example.crest_app.views.home import login
from example.crest_app.views.home import logout
from example.crest_app.views.home import login
import social.apps.django_app.urls as social

urlpatterns = [
    url(r'^$', login_required(HomeView.as_view(), redirect_field_name=None)),
    url(r'^login/$', login, name='user_login'),
    url(r'^logout/$', logout, name='user_logout'),
    url('', include(social, namespace='social')),
]
