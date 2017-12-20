from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<episode_id>[0-9]+)/$', views.index, name='index'),
]
