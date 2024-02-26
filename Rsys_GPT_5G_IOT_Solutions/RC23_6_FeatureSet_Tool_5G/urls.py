from django.contrib import admin
from django.urls import path
from . import RC23_6_FeatureSet_Views


urlpatterns = [
    path('', RC23_6_FeatureSet_Views.featureset_homepage, name = "homepage"),
]