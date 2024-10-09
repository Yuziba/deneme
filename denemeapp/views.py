from django.shortcuts import render
from django.views.generic import TemplateView
# Kullanıcıdan veri almak için form



class MainView(TemplateView):
    template_name = "denemeapp/index.html"