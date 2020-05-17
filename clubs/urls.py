from . import views
from django.urls import path
from .views import club, clubdetail
# , FootballClubDetailView, FootballClubCreateView

app_name = "clubs"

urlpatterns = [
    path('', views.index, name='premier-home'),
    path('clubs/', views.club, name='club-list'),
    path('clubs/<slug:slug>/', views.clubdetail, name='club-detail'),
]