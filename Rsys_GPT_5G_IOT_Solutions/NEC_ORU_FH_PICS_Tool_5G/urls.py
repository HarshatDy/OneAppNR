from django.contrib import admin
from django.urls import path
from . import NEC_ORU_FH_PICS_views


urlpatterns = [
    path('', NEC_ORU_FH_PICS_views.nec_oru_homepage, name = "homepage"),
]