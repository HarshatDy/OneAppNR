from django.contrib import admin
from django.urls import path
from . import PTP_Delay_Views


urlpatterns = [
    path('', PTP_Delay_Views.ptp_delay_homepage, name = "Homepage"),
    path('ptp_delay_calculation', PTP_Delay_Views.ptp_delay_calculation, name="ptp_delay_calculation"),
]

