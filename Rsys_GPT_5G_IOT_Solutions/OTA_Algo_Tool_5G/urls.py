from django.contrib import admin
from django.urls import path
from . import OTA_Algo_Views


urlpatterns = [
    path('', OTA_Algo_Views.ota_algo_homepage, name = "Homepage"),
    path('ota_calculation', OTA_Algo_Views.ota_algo_calculation, name="ota_calculation"),
]

