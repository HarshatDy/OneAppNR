from django.contrib import admin
from django.urls import path
from . import NR_TBS_Views


urlpatterns = [
    path('', NR_TBS_Views.tbs_homepage, name = "Homepage"),
    path('tbs_calculation', NR_TBS_Views.calculate_tbs, name="tbs_calculation"),
]

