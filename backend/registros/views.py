from rest_framework import generics
from .models import Registro, AlimentoConsumido
from .serializers import RegistroSerializer, AlimentoConsumidoSerializer

class RegistroListCreateView(generics.ListCreateAPIView): 
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    
    def get_queryset(self): 
        """
        Permite filtrar registros por fecha en la URL: 
        /api/registros/?fecha=2026-11-11
        """

        queryset = super().get_queryset()
        fecha = self.request.query_params.get('fecha')
        if fecha: 
            queryset = queryset.filter(fecha=fecha)
        return queryset


class RegistroDetailView(generics-RetrieveUpdateDestroyAPIView): 
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer


class AlimentoConsumidoCreateView(generics.CreateAPIView): 
    queryset = AlimentoConsumido.objects.all()
    serializer_class = AlimentoConsumidoSerializer


class AlimentoConsumidoDetailView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = AlimentoConsumido.objects.all()
    serializer_class = AlimentoConsumidoSerializer

        