# backend/monitor/serializers.py
from rest_framework import serializers
from .models import Server, ServerMetrics

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'

class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerMetrics
        fields = '__all__'