

from django.contrib import admin
from django.urls import path
from . import NEC_ORAN_CUSPlane_SOC_8T8R_NEC_RU_Views


urlpatterns = [
    path('', NEC_ORAN_CUSPlane_SOC_8T8R_NEC_RU_Views.nec_oran_homepage, name = "homepage"),
]