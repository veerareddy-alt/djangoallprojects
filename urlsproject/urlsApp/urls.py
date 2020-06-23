from django.urls import path
from urlsApp import views

urlpatterns = [
    path('hybjob/', views.hybjobinfo),
    path('punejob/', views.punejobinfo),
    path('chennaijob/', views.chennaijobinfo),
    path('mumbaijob/', views.mumbaijobinfo),
]
