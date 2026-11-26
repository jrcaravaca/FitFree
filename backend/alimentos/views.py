from rest_framework import generics, permissions
from .models import Alimento
from .serializers import AlimentoSerializer

class AlimentoListCreateView(generics.ListCreateAPIView): 
    serializer_class = AlimentoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self): 
        queryset = Alimento.objects.all().order_by('nombre')
        search = self.request.query_params.get('search')
        if search: 
            queryset = queryset.filter(nombre__icontains=search)
        return queryset

class AlimentoDetailView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    permission_classes = [permissions.IsAuthenticated]