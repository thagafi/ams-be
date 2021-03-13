from django.db import models
from computers.models import CPUModel, RamSize, Brand, OS
from formations.models import Squads
from django.conf import settings

# Create your models here.
class ServersModel(models.Model):
    CHOICES = (
        ('GEN', 'General Network'),
        ('TSN', 'Technical Support Network'),
        ('SEC', 'Secure Network')
    )
    server_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True)
    date = models.DateField(auto_now=True)
    cpu = models.ForeignKey(CPUModel, on_delete=models.CASCADE, related_name="server_cpu_type")
    ram = models.ForeignKey(RamSize, on_delete=models.CASCADE, related_name="server_ram_size")
    status = models.BooleanField(default=True)
    network = models.CharField(max_length=200, choices= CHOICES)
    os = models.ForeignKey(OS, on_delete=models.CASCADE, related_name="server_os_type")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="server_brand_company")
    
    def __str__(self):
        return self.server_name