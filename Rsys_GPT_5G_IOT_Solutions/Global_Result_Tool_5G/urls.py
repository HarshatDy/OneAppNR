from django.contrib import admin
from django.urls import path
from . import Global_Result_Views


urlpatterns = [
    path('', Global_Result_Views.global_result_homepage, name = "homepage"),
    path('du_calculation', Global_Result_Views.global_result, name="global_result"),
]