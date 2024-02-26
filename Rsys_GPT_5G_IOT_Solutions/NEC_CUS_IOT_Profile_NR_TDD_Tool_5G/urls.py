from django.contrib import admin
from django.urls import path
from . import NEC_CUS_IOT_Profile_NR_TDD_Views


urlpatterns = [
    path('', NEC_CUS_IOT_Profile_NR_TDD_Views.nec_cus_homepage, name = "homepage"),
]