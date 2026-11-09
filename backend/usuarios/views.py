from rest_framework import generics
from .models import PerfilUsuario, ObjetivoUsuario
from .serializers import PerfilUsuarioSerializer, ObjetivoUsuarioSerializer

class PerfilUsuarioDetailView(generics.RetrieveUpdateAPIView): 
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer

class ObjetivoUsuarioDetailView(generics.RetrieveUpdateAPIView): 
    queryset = ObjetivoUsuario.objects.all()
    serializer_class = ObjetivoUsuarioSerializer


