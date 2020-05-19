from . import views
from django.urls import path
from .views import club, clubdetail, allplayers, playerdetail
# , FootballClubDetailView, FootballClubCreateView

app_name = 'clubs'
app_name = 'players'

urlpatterns = [
    path('', views.index, name='premier-home'),
    path('clubs/', views.club, name='club-list'),
    path('clubs/<slug:slug>/', views.clubdetail, name='club-detail'),
    path('players/', views.allplayers, name='allplayers'),
    path('players/<slug:slug>/', views.playerdetail, name='player-detail'),
    
    # path('', views.player, name='players-home'),
    # path('clubs/<slug:clubdetail_slug>/', views.clubdetail, name='club-detail'),
    # path('clubs/<slug:clubdetail_slug>/<slug:clubdetail_slug>/<slug:players_slug>/', views.players, name='players'),
    # path('clubs/<slug:clubdetail_slug>/<slug:clubdetail_slug>/<slug:players_slug>/<slug:playerdetail_slug>/', views.playerdetail, name='player-detail'),
    

]