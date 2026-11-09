from rest_framework import generics
from .models import Alimento
from .serializers import AlimentoSerializer

class AlimentoListCreateView(generics.ListCreateAPIView): 
    queryset = Alimento.objects.filter(estado='APROBADO')
    serializer_class = AlimentoSerializer

class AlimentoDetailView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer

