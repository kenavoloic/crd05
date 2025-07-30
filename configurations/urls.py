from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil),
    path('liste', views.liste_clubs)
]
