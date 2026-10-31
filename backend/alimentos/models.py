from django.db import models
from django.contrib.auth.models import User

#Opciones de Origen
ORIGEN_CHOICES = [
    ('PROPIA', 'Base de Datos Propia'), 
    ('OPENFOODFACTS', 'Open Food Facts'), 
    ('USUARIO', 'Propuesto por Usuario')
]

#Opciones de Moderación
ESTADO_CHOICES = [
    ('PROPUESTO', 'Propuesto'),
    ('EN_REVISION', 'En revisión'),
    ('APROBADO', 'Aprobado'),
    ('RECHAZADO', 'Rechazado')
]

class Alimento(models.Model): 
    nombre = models.CharField(max_length=150)

    #Valores nutricionales por 100g
    calorias = models.PositiveIntegerField(help_text="Calorías por cada 100g")
    proteinas = models.DecimalField(max_digits=5, decimal_places=2, help_text='Gramos por cada 100g')
    carbohidratos = models.DecimalField(max_digits=5, decimal_places=2, help_text='Gramos por cada 100g')
    grasas = models.DecimalField(max_digits=5, decimal_places=2, help_text='Gramos por cada 100g')

    #Datos opcionales y de origen
    codigo_barras = models.CharField(max_length=50, unique=True, null=True, blank=True)
    origen = models.CharField(max_length=20, choices=ORIGEN_CHOICES, default='PROPIA')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='APROBADO')

    #Usuario que propone el alimento y fotografía
    creadord = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='alimentos_creados')
    foto = models.ImageField(upload_to='alimentos/', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} ({self.calorías}) kcal/100g'