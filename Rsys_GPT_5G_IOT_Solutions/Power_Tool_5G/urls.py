from django.contrib import admin
from django.urls import path
from . import Power_Tool_Views


urlpatterns = [
    path('', Power_Tool_Views.power_homepage, name = "Homepage"),
]

