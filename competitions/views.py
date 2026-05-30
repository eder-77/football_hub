from rest_framework import generics
from .models import Tournament,Team,Match
from .serializers import TournamentSerializer,TeamSerializer,MatchSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class TournamentListCreateAPIView(generics.ListCreateAPIView):
  queryset=Tournament.objects.all()
  serializer_class=TournamentSerializer

class TeamListCreateAPIView(generics.ListCreateAPIView):
  queryset=Team.objects.all()
  serializer_class=TeamSerializer

class MatchListCreateAPIView(generics.ListCreateAPIView):
  queryset=Match.objects.all()
  serializer_class=MatchSerializer 

class GenerateFixturesView(APIView):
  def post(self,request,tournament_id):

    tournament=get_object_or_404(Tournament,id=tournament_id)
    teams=list(Team.objects.filter(tournament=tournament))
    if len(teams)<2:
      return Response(
        {"error:you need 2 teams or more to generate fixtures"},
        status=status.HTTP_400_BAD_REQUEST
      )
    if tournament.format==Tournament.FormatChoices.LEAGUE:
      return self.generate_laegue_fixtures(tournament,teams)
    
  def generate_laegue_fixtures(self,tournament,teams):

    if len(teams)%2 !=0:
      teams.append(None)
    
    nbr_rounds=len(teams)-1
    matches_per_round=len(teams)//2

    for num_round in range(1,len(teams)):

      for i in range(matches_per_round):
        home=teams[i]
        away=teams[len(teams)-1-i]

        if home is not None and away is not None:
          Match.objects.create(
            tournament=tournament,
            home_team=home,
            away_team=away,
            round_number=num_round
          )

      teams=[teams[0]]+[teams[-1]]+teams[1:-1]   

    return Response(
      {"message":f"Successfully generated fixtures for {nbr_rounds} rounds."},
      status=status.HTTP_201_CREATED
    )
    

     



