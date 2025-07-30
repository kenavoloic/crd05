from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return HttpResponse("Liste de joueurs du top 14 saison 2024-2025")
# Create your views here.
