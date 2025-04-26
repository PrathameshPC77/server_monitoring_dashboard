from django.shortcuts import render

# Create your views here.
# backend/monitor/views.py
from django.shortcuts import render
from .models import Server, ServerMetrics

from django.shortcuts import render
from .models import Server, ServerMetrics
from datetime import datetime, timedelta

def dashboard(request):
    # Get all servers and metrics
    servers = Server.objects.all()
    metrics = ServerMetrics.objects.order_by('-timestamp')[:50]  # Latest 50
    
    #alert counts 
    alert_counts = {
        'critical': ServerMetrics.objects.filter(alert_level='critical').count(),
        'medium': ServerMetrics.objects.filter(alert_level='medium').count(),
        'low': ServerMetrics.objects.filter(alert_level='low').count(),
    }
    
    # prepare the chart data
    timestamps = [m.timestamp.strftime('%H:%M') for m in metrics]
    cpu_data = [m.cpu_usage for m in metrics]
    memory_data = [m.memory_usage for m in metrics]
    disk_data = [m.disk_usage for m in metrics]
    network_in_data = [m.network_in for m in metrics]
    
    cpu_avg = min(sum(cpu_data)/len(cpu_data) if cpu_data else 0, 100)
    cpu_available = max(100 - cpu_avg, 0)

    return render(request, 'dashboard.html', {
        'servers': servers,
        'metrics': metrics,
        'alerts': alert_counts,
        'timestamps': timestamps,
        'cpu_data': cpu_data,
        'memory_data': memory_data,
        'disk_data': disk_data,
        'network_in_data': network_in_data,
        'cpu_avg': cpu_avg,
        'cpu_available': cpu_available,
    })