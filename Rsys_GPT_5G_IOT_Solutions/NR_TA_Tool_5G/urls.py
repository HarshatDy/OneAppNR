from django.contrib import admin
from django.urls import path
from . import NR_TA_Views


urlpatterns = [
    path('', NR_TA_Views.ta_homepage, name = "Homepage"),
    path('ta_calculation', NR_TA_Views.calculate_5g_timing_advance_distance, name="ta_calculation"),
]

