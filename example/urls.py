from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from example.crest_app.views.home import HomeView # added example.'' for py3 support

urlpatterns = patterns(
    '',
    url(r'^$', login_required(HomeView.as_view(), redirect_field_name=None)),
    url(r'^login/$', 'example.crest_app.views.home.login', name='user_login'),
    url(r'^logout/$', 'example.crest_app.views.home.logout', name='user_logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
