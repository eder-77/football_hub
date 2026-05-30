from rest_framework import serializers
from .models import Tournament,Match,Team

class TournamentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Tournament
    fields=['id','name','format','created_at']

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model=Team
    fields=['id','tournament','name','manager']

class MatchSerializer(serializers.ModelSerializer):
  class Meta:
    model=Match
    fields=['id','tournament','home_team','away_team','home_score','away_score','is_played']        