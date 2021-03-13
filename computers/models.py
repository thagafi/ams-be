from django.db import models
from formations.models import Wings, Squads
from django.conf import settings


class CPUModel(models.Model):
    type = models.CharField(max_length=150)
    
    def __str__(self):
        return self.type

class RamSize(models.Model):
    size = models.CharField(max_length=150)
    
    def __str__(self):
        return self.size

class MonitorSize(models.Model):
    monitor = models.CharField(max_length=150)
    
    def __str__(self):
        return self.monitor

class OS(models.Model):
    os = models.CharField(max_length=150)
    
    def __str__(self):
        return self.os

class Brand(models.Model):
    company = models.CharField(max_length=150)
    
    def __str__(self):
        return self.company


class ComputersModel(models.Model):
    computer_name = models.CharField(max_length=200, unique=True)
    squad = models.ForeignKey(Squads, on_delete=models.CASCADE, related_name="squad_location", null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True)
    date = models.DateField(auto_now=True)
    cpu = models.ForeignKey(CPUModel, on_delete=models.CASCADE, related_name="cpu_type")
    ram = models.ForeignKey(RamSize, on_delete=models.CASCADE, related_name="ram_size")
    monitor_size = models.ForeignKey(MonitorSize, on_delete=models.CASCADE, related_name="monitor_size")
    os = models.ForeignKey(OS, on_delete=models.CASCADE, related_name="os_type")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand_company")
    
    def __str__(self):
        return self.computer_name
    