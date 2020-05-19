from django.shortcuts import render, get_object_or_404, redirect
from .models import Club, Player


def index(request):
    return render(request, 'clubs/index.html', {})

def club(request):
    clubs = Club.objects.all()

    context = {
        'clubs': clubs
    }
    return render(request, 'clubs/footballclub_list.html', context)

def clubdetail(request, slug=None):
    instance = get_object_or_404(Club, slug=slug)
    club = Club.objects.get(slug=slug)

    context = {
        'club': club,
    }
    return render(request, 'clubs/footballclub.html', context)


def allplayers(request, slug=None):
    allplayers = Player.objects.all()

    context = {
        'allplayers': allplayers,
    }
    return render(request, 'clubs/squad/footballsquad.html', context)

def playerdetail(request, slug=None):
    instance = get_object_or_404(Player, slug=slug)
    player = Player.objects.get(slug=slug)

    context = {
        'player': player,
    }
    return render(request, 'clubs/squad/footballplayer.html', context)