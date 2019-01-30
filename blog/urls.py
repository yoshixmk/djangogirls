from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('^$', views.post_list, name='post_list'),
]
