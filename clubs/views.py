from django.shortcuts import render, redirect
from .models import Club


def index(request):
    return render(request, 'clubs/index.html', {})

def club(request):
    clubs = Club.objects.all()

    context = {
        'clubs': clubs
    }
    return render(request, 'clubs/footballclub_list.html', context)

def clubdetail(request, slug):
    club = Club.objects.get(slug=slug)

    context = {
        'club': club,
    }
    return render(request, 'clubs/footballclub.html', context)

