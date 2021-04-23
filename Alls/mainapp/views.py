import uuid
import requests

from urllib.parse import urlencode
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Chin, Di, Corporation, RatingStar, Rating


class allianceView(View):

    def get(self, request):
        corp = Corporation.objects.all()
        return render(request, 'alliance.html', {"corp": corp})


class LoginWithEvo(View):
    # авторизация

    def get(self, request, *args, **kwargs):
        self.EVE_ID = "9697b7f08948431fb4c30f1f35efb973"
        self.EVE_SECRET_KEY = "SoUMcAqEYkYPleqVz4HRdaw7ln7Og5ZXHGthNoOx"
        self.SOCIAL_EVE_AUTH_URL = "https://login.eveonline.com/v2/oauth/authorize/?"
        self.REDIRECT_URI = "http://127.0.0.1:8000/eve_login/"
        self.EVE_AUTH_TOKEN = "https://login.eveonline.com/v2/oauth/token/?"
        self.EVE_VERIFY = "https://login.eveonline.com/oauth/verify/"


        params = {
            "response_type": "code",
            "redirect_uri": self.REDIRECT_URI,
            "client_id": self.EVE_ID,
            "state": uuid.uuid4(),
            "scope": "publicData esi-characters.read_standings.v1 esi-mail.read_mail.v1",
        }
        code = request.GET.get("code")
        print("CODE", request.GET)
        print("CODE", code)

        if code:
            params.update(
                {
                    "client_secret": self.EVE_SECRET_KEY,
                    "code": code,
                    "grant_type": "authorization_code",
                }
            )

            try:
                resp = requests.post(self.EVE_AUTH_TOKEN, data=params).json()
                token = resp.get("access_token")
                print(token)
                if token:
                    resp = requests.get(
                        self.EVE_VERIFY,
                        headers={"Authorization": f"Bearer {token}"},
                    ).json()
                    print(resp)
                    return HttpResponseRedirect("/")

            except Exception as e:
                print(e)

        return HttpResponseRedirect(self.SOCIAL_EVE_AUTH_URL + urlencode(params))


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
