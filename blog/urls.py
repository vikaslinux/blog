__author__ = 'vika'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='mainpage'),
]