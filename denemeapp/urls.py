from django.urls import path
from . import views

#-------------bunu unutma
App_name = 'denemeapp'


urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("goster/", views.goster, name="goster"),
    path("girdi/", views.girdi, name="girdi"),
] 
