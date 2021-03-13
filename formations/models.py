from django.db import models
from django.conf import settings

class Wings(models.Model):
    wing_name = models.CharField(max_length=200)
    wing_commander = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="wing_commander")
    wing_coordinator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="wing_coordinator")
    
    def __str__(self):
        return self.wing_name



class Squads(models.Model):
    Squad_name = models.CharField(max_length=200)
    wing = models.ForeignKey(Wings, on_delete=models.CASCADE, related_name="wing", null=True)
    Squad_commander = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="squad_commander")
    Squad_coordinator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="squad_coordinator")
    
    def __str__(self):
        return self.Squad_name