from django.contrib import admin
from django.urls import path
from . import RC23_6_Featurebitmap_Views


urlpatterns = [
    path('', RC23_6_Featurebitmap_Views.bitmap_homepage, name = "homepage"),
]