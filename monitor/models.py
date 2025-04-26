from django.db import models

# Create your models here.
from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    status = models.BooleanField(default=True)
    location = models.CharField(max_length=100, default="Data Center A")

class ServerMetrics(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    cpu_usage = models.FloatField()  # %
    memory_usage = models.FloatField()  # %
    disk_usage = models.FloatField()  # %
    network_in = models.FloatField()  # MB/s
    network_out = models.FloatField()  # MB/s
    alert_level = models.CharField(max_length=10, choices=[
        ('critical', 'Critical'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ],
        null=True,  
        blank=True  
    )
    timestamp = models.DateTimeField(auto_now_add=True)