from django.shortcuts import render
from django.http import HttpResponse
from .models import Club


def accueil(request):
    return HttpResponse("Liste de joueurs du top 14 saison 2024-2025")

def liste_clubs(request):
    context = {}
    tous = Club.objects.all()
    context['clubs'] = tous
    context['titre'] = 'Accueil'
    return render(request, 'configurations/liste_clubs.html', context)

    #if request.method == 'POST':
        
