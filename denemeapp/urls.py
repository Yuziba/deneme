from django.urls import path
from . import views

#-------------bunu unutma
App_name = 'denemeapp'


urlpatterns = [
    path("", views.index),
    path("", views.index, name="index"),
    path("blog/<int:id>", views.blog, name="blog"),
] 

