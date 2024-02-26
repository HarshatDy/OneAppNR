from django.contrib import admin
from django.urls import path
from . import Sunwave_IOT_Paramter_Views


urlpatterns = [
    path('', Sunwave_IOT_Paramter_Views.sunwave_homepage, name = "homepage"),
]