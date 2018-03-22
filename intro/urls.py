from django.conf.urls import url, include
from . import views

urlpatterns = [
               url(r'^', views.index, name = 'intro'),
               url(r'^algorithm', views.alg, name = 'algorithm'),
]
