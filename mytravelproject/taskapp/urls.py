from django.contrib import admin
from django.urls import path, include

from.import views

urlpatterns = [

    #path('',views.home,name='home'),
    #path('about',views.about,name='about'),
    #path('contact', views.contact, name='contact'),
#path('details', views.details, name='details'),
#path('thanks', views.thanks, name='thanks'),
   # path('',views.input,name='input'),
    #path('algebra/',views.result,name='result'),
path('',views.webpage,name='webpage'),
]
