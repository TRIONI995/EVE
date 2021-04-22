from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Chin, Di, Corporation, RatingStar, Rating


class allianceView(View):

    def get(self, request):
        corp = Corporation.objects.all()
        return render(request, 'alliance.html', {"corp": corp})

def index(request):
    return render(request, 'download.html')

#def home(request):
    #return render(request, 'home.html')


class controlView(View):

    def get(self, request):
        control = Chin.objects.all()
        return render(request, 'control.html', {"control": control})


def promotions(request):
    return render(request, 'home.html')


def rent(request):
    return render(request, 'home.html')


def inst(request):
    return render(request, 'home.html')


def gid(request):
    return render(request, 'home.html')


def download(request):
    return render(request, 'downloads.html')


def login(request):
    return render(request, 'login.html')





def login(request):
    return render(request, 'login.html')




def info(request):
    return render(request, 'info.html')
