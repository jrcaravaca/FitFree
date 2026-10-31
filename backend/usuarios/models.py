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
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.PositiveIntergerField() #en centimetros
    sexo = models.Charfield(max_length=1, choices=SEXO_CHOICES)
    nivel_actividad = models.Charfield(max_length=20, choices=ACTIVIDAD_CHOICES, default='MODERADO')

    def __str__(self): 
        return f"Perfil de {self.usuario.username}"

class ObjetivoUsuario(models.Model): 
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='objetivo')
    calorias = models.PositiveIntergerField()
    proteinas = models.PositiveIntergerField() #en gramos
    carbohidratos = models.PositiveIntergerField() # en gramos
    grasas = models.PositiveIntergerField() #en gramos

    def __str__(self): 
        return f"Objetivo de {self.usuario.username} ({self.calorias} kcal)"