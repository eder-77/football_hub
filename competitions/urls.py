from django.urls import path 
from .views import TournamentListCreateAPIView,TeamListCreateAPIView,MatchListCreateAPIView,GenerateFixturesView

urlpatterns=[
  path('api/tournaments/',TournamentListCreateAPIView.as_view(),name='api_tournament_list_create'),
  path('api/teams/',TeamListCreateAPIView.as_view(),name='api_team_list_create'),
  path('api/matches/',MatchListCreateAPIView.as_view(),name='api_match_list_create'),
  path('tournamemt/<int:tournament_id>/',GenerateFixturesView.as_view(),name='generate_fixtures')
]