from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.home),
    url(r'^process$', views.process),
    url(r'^results$', views.results),
    url(r'^add_friend$', views.add_friend),
    url(r'^goback$', views.goback),
]