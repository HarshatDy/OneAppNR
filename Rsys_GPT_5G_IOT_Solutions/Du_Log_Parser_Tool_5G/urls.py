from django.contrib import admin
from django.urls import path
from . import Du_Log_Parser_Views


urlpatterns = [
    path('', Du_Log_Parser_Views.du_log_homepage, name = "Homepage"),
    path('du_calculation', Du_Log_Parser_Views.du_log_parsing, name="du_calculation"),
]

