from django.contrib import admin
from django.urls import path, include

from mytodoapp import views

urlpatterns = [
    # path('',views.demo,name='demo'),
    # path('details', views.details, name='details'),
    path('cbvhome/',views.Taskview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(),name='cbvdelete'),

    path('delete/<int:taskid>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),

]
