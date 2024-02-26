from django.contrib import admin
from django.urls import path
from . import Frequency_Tool_Views


urlpatterns = [
    path('', Frequency_Tool_Views.freq_homepage, name = "Homepage"),
    path('freq_calculation', Frequency_Tool_Views.freq_calculation, name="freq_calculation"),
    # path('freq_table_homepage', Frequency_Tool_Views.freq_table_homepage, name="freq_table_homepage"),
    path('freq_table', Frequency_Tool_Views.freq_value_homepage, name="freq_value_homepage"),
    path('freq_value', Frequency_Tool_Views.freq_value, name="freq_value"),
]

