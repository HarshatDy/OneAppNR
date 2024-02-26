from django.contrib import admin
from django.urls import path
from . import NR_Cell_Identity_Views


urlpatterns = [
    path('', NR_Cell_Identity_Views.cell_identity_homepage, name = "Homepage"),
    path('cell_identity', NR_Cell_Identity_Views.calculate_nci, name="cell_identity"),
]

