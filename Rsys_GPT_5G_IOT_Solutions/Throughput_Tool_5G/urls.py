from django.contrib import admin
from django.urls import path
from . import Througput_Tool_Views


urlpatterns = [
    path('', Througput_Tool_Views.throughput_homepage, name = "Homepage"),
    path('tpt_calculation', Througput_Tool_Views.throughput_calculation, name ="throughput_calculation"),
]

