from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path 
from . import All_Tools_Views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', All_Tools_Views.homepage, name = "Homepage"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

