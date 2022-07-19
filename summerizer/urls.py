from django.contrib import admin
from django.urls import path
from summerizer import views

urlpatterns = [
    path("", views.summerize, name = "summerize"),
    path("about", views.about, name = "about"),
    path("paragraph", views.paragraph, name = 'paragraph'),
]