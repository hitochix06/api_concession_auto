from rest_framework import viewsets
from .models import Concession, Vehicule
from .serializers import ConcessionSerializer, VehiculeSerializer

class ConcessionViewSet(viewsets.ModelViewSet):
    queryset = Concession.objects.all()
    serializer_class = ConcessionSerializer

class VehiculeViewSet(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer

class ConcessionVehiculesViewSet(viewsets.ModelViewSet):
    serializer_class = VehiculeSerializer

    def get_queryset(self):
        return Vehicule.objects.filter(concession_id=self.kwargs['concession_pk'])

    def perform_create(self, serializer):
        serializer.save(concession_id=self.kwargs['concession_pk']) 