from django.contrib import admin
from django.urls import path

from . import Qual_Log_Views


urlpatterns = [
    path('', Qual_Log_Views.qual_log_homepage, name = "Homepage"),
    path('qual_log_calculation', Qual_Log_Views.qual_log_calculation, name="qual_log_calculation"),
]

