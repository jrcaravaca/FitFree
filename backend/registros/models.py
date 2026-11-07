from django.db import models
from datetime import date
from django.contrib.auth.models import User
from alimentos.models import Alimento


# Elecciones posibles de comidas
COMIDA_CHOICES = [
    ('DESAYUNO', 'Desayuno'), 
    ('SNACK', 'Snack'), 
    ('COMIDA', 'Comida'), 
    ('MERIENDA', 'Merienda'),
    ('CENA', 'Cena'),
]

class Registro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registros')
    fecha = models.DateField(default=date.today)
    comida = models.CharField(max_length=15, choices=COMIDA_CHOICES)

    class Meta: 
        #Restricción para que un usuario solo tenga 1 registro por tipo y fecha
        constraints = [
            models.UniqueConstraint(fields=['usuario','fecha','comida'], name='unique_registro_usuario_fecha_comida')
        ]
        ordering = ['-fecha', 'comida']

        def __str__(self): 
            return f"{self.usuario.username} - {self.comida} ({self.fecha})"

class AlimentoConsumido(models.Model): 
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name='alimentos_consumidos')
    alimento = models.ForeignKey(Alimento, on_delete=models.PROTECT, related_name='consumos')
    cantidad_gramos = models.PositiveIntegerField(help_text='Cantidad consumida en gramos')

    def __str__(self): 
        return f"{self.cantidad_gramos}g de {self.alimento.nombre} en {self.registro.comida}"