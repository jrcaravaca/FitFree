from django.db import models
from django.contrib.auth.models import User

#Opciones fijas de sexo biologico
SEXO_CHOICES = [
    ('H', 'Hombre'),
    ('M', 'Mujer')
]

#Opciones fijas de nivel de actividad
ACTIVIDAD_CHOICES = [
    ('SEDENTARIO', 'Sedentario (poco o ningún ejercicio)'),
    ('LIGERO', 'Ligero (1-3 días/semana)'), 
    ('MODERADO', 'Moderado (3-5 días/semana)'),
    ('FUERTE', 'Fuerte (6-7 días/semana)')
]

class PerfilUsuario(models.Model): 
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2) #DecimalField para guardar datos exactos. (Float mete redondeos)
    altura = models.PositiveIntegerField() #en centimetros
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    nivel_actividad = models.CharField(max_length=20, choices=ACTIVIDAD_CHOICES, default='MODERADO')

    def __str__(self): 
        return f"Perfil de {self.usuario.username}"

class ObjetivoUsuario(models.Model): 
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='objetivo')
    calorias = models.PositiveIntegerField()
    proteinas = models.PositiveIntegerField() #en gramos
    carbohidratos = models.PositiveIntegerField() # en gramos
    grasas = models.PositiveIntegerField() #en gramos

    def __str__(self): 
        return f"Objetivo de {self.usuario.username} ({self.calorias} kcal)"