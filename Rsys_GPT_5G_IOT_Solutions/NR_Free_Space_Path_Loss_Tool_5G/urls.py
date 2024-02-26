from django.contrib import admin
from django.urls import path
from . import NR_Free_Space_Path_Loss_Views


urlpatterns = [
    path('', NR_Free_Space_Path_Loss_Views.pathloss_homepage, name = "Homepage"),
    path('pathloss_calculation', NR_Free_Space_Path_Loss_Views.calculate_fspl, name="pathloss_calculation"),
]

