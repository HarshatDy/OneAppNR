from django.contrib import admin
from django.urls import path
from . import NR_EPRE_Views


urlpatterns = [
    path('', NR_EPRE_Views.epre_homepage, name = "Homepage"),
    path('epre_calculation', NR_EPRE_Views.calculate_epre_power, name="epre_calculation"),
]

