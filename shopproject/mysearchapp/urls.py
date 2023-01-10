from django.urls import path

from mysearchapp import views

app_name='mysearchapp'

urlpatterns = [

   path('',views.searchresult,name='Searchresult'),

]