from django.contrib import admin
from django.urls import path
from . import RE_Mapping_Views


urlpatterns = [
    path('', RE_Mapping_Views.re_mapping_homepage, name = "Homepage"),
    path('re_mapping_calculation', RE_Mapping_Views.re_mapping_calculation, name="re_calculation"),
]

