from django.contrib import admin
from django.urls import path
from . import Link_Budget_Views


urlpatterns = [
    path('', Link_Budget_Views.link_budget_homepage, name = "homepage"),
    path('link_budget_calculation', Link_Budget_Views.link_budget_calculation, name="link_budget"),
]