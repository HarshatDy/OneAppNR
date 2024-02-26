from django.contrib import admin
from django.urls import path
from . import NR_ARFCN_Views


urlpatterns = [
    path('', NR_ARFCN_Views.nr_arfcn_homepage, name = "homepage"),
    path('nr_arfcn_calculation', NR_ARFCN_Views.nr_arfcn_calculation, name="nr_arfcn_calculation"),
]