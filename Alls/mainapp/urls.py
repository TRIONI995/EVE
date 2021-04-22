from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    #path('', views.home, name='home'),
    path('alliance/', views.allianceView.as_view(), name='alliance'),
    path('control', views.controlView.as_view(), name='control'),
    path('promotions/', views.promotions, name='promotions'),
    path('rent/', views.rent, name='rent'),
    path('inst/', views.inst, name='inst'),
    path('gid/', views.gid, name='gid'),
    path('contact/', views.contact, name='contact'),
    path('download/', views.download, name='download'),


    path('login/', views.login, name='login'),
    path('info/', views.info, name='info'),
]