from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tournament(models.Model):
  class FormatChoices(models.TextChoices):
    LEAGUE='LEAGUE','League'
    KNOCKOUT='KNOCKOUT','Knockout'
    GROUP_KNOCKOUT='GROUP_KNOCKOUT','Group Stage + Knockout'
  name=models.CharField(max_length=100)
  format=models.CharField(max_length=50,choices=FormatChoices.choices,default=FormatChoices.LEAGUE)
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  
class Team(models.Model):
  tournament=models.ForeignKey(Tournament,on_delete=models.CASCADE,related_name='teams')
  name=models.CharField(max_length=100)
  manager=models.ForeignKey(User,on_delete=models.CASCADE,related_name='managed_teams')

  def __str__(self):
    return f"{self.name} ({self.tournament})"
  
class Match(models.Model):
  tournament=models.ForeignKey(Tournament,on_delete=models.CASCADE,related_name='matches')
  home_team=models.ForeignKey(Team,on_delete=models.CASCADE,related_name='home_matches')
  away_team=models.ForeignKey(Team,on_delete=models.CASCADE,related_name='away_matches')
  home_score=models.IntegerField(default=0)
  away_score=models.IntegerField(default=0)
  is_played=models.BooleanField(default=False)
  round_number=models.IntegerField(default=1)

  def __str__(self):
    return f"{self.home_team.name} vs {self.away_team.name}"