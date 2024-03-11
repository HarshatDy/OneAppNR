from django.contrib import admin
from django.urls import path
from . import Du_Log_Parser_Views


urlpatterns = [
    path('', Du_Log_Parser_Views.du_log_homepage, name = "Homepage"),
    path('du_calculation', Du_Log_Parser_Views.du_log_parsing, name="du_calculation"),
    path('/cu_du_counters', Du_Log_Parser_Views.cu_du_counters, name="cu_du_counters"),
    path('/du_kpi', Du_Log_Parser_Views.du_kpi, name="du_kpi"),
    path('/l1_timing', Du_Log_Parser_Views.l1_timing, name="l1_timing"),
    path('/pm_counters', Du_Log_Parser_Views.pm_counters, name="pm_counters"),
    path('/process_monitor',Du_Log_Parser_Views.process_monitor, name="process_monitor"),
]

