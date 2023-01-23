from django.urls import path
from django.http import HttpResponse
from ProfileApp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('history', views.history, name="history"),
    path('interests', views.interests , name='interests'),
    path('career', views.career , name= 'career'),
    path('rolemodel', views.rolemodel,name= 'rolemodel'),
    path('study',views.study,name='study'),

]
