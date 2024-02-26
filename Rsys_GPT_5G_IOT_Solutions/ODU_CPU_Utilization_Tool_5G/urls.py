
from django.contrib import admin
from django.urls import path
from . import ODU_CPU_Views


urlpatterns = [
    path('', ODU_CPU_Views.odu_cpu_homepage, name = "homepage"),
    path('odu_cpu_utilization', ODU_CPU_Views.odu_cpu_calculation, name="odu_cpu_utilization"),
]