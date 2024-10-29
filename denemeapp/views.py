from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . import forms
from . import models
# Kullanıcıdan veri almak için form



class MainView(TemplateView):
    template_name = "denemeapp/index.html"

def goster(request):
    return render(request, "denemeapp/goster.html")

def girdi(request):
    return render(request, "denemeapp/girdi.html")

def veri_kaydet_gonder_view(request):
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        message = request.POST.get("message")
        veri_kaydet = models.AaModel(nickname=nickname,
                                     message=message)
        veri_kaydet.save()
        return redirect('goster')
    veri_kaydet_gonder_list = models.AaModel.objects.all()
    return render(request, "denemeapp/girdi.html", {'veri_kaydet_gonder_':veri_kaydet_gonder_list})
"""
def aaView(request):
    if request.method == "POST":
        form = forms.DenemeForm(request.POST)
        if form.is_valid():
            nick = form.cleaned_data["nick"]
            mesaj = form.cleaned_data["mesaj"]
            models.AaModel.objects.create(nick=nick, mesaj=mesaj)
        else:
            print("ERRORR")
            return render(request, "denemeapp/index.html", context={"form":form})
    else:
        form = forms.DenemeForm()
        return render(request, "denemeapp/index.html", context={"form":form})"""