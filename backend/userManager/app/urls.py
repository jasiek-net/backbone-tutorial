from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'userManager.views.home', name='home'),

    url(r'^users/$', views.users, name='users'),
    url(r'^users/(?P<id>[0-9]+)$', views.user, name='user')
]
