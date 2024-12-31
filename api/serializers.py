from rest_framework import serializers
from .models import Concession, Vehicule

class ConcessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concession
        fields = ['id', 'nom', 'code_postal', 'adresse']

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__' 