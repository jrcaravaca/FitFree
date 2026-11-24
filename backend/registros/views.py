from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Registro, AlimentoConsumido
from .serializers import RegistroSerializer, AlimentoConsumidoSerializer

class RegistroListCreateView(generics.ListCreateAPIView): 
    serializer_class = RegistroSerializer
    permissions_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self): 
        queryset = Registro.objects.filter(usuario=self.request.user).order_by('fecha', 'id')
        fecha = self.request.query_params.get('fecha')
        if fecha: 
            queryset = queryset.filter(fecha=fecha)
        return queryset

        def perform_create(self, serializer): 
            # Cuando REACT envie los datos, Django inyectará el ususario del token JWT automáticamente
            serializer.save(usuario=self.request.user)


class RegistroDetailView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = RegistroSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self): 
        return Registro.objects.filter(usuario=self.request.user)


class AlimentoConsumidoCreateView(generics.ListCreateAPIView): 
    serializer_class = AlimentoConsumidoSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self): 
        return AlimentoConsumido.objects.filter(registro__usuario=self.request.user)

    def perform_create(self, serializer): 
        # Validación cruzada, evita que alguien manipule el ID de registro den el JSON para colar alimentos en la comida de otra persona
        registro = serializer.validated_data['registro']
        if registro.usuario != self.request.user: 
            raise ValidationError("No tienes permiso para añadir alimentos a este registro")
        serializer.save()


class AlimentoConsumidoDetailView(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = AlimentoConsumidoSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self): 
        return AlimentoConsumido.objects.filter(registro__usuario=self.request.user)        