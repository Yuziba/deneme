from django.shortcuts import render
from django.http import HttpResponse
# Kullanıcıdan veri almak için form

def index(request):
    return render(request, "denemeapp/index.html")

def blog(request, id):
    return render(request, "denemeapp/blog.html",{
        "id": id
    })
