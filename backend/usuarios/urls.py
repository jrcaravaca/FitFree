from django.urls import path
from .views import PerfilUsuarioDetailView, ObjetivoUsuarioDetailView, RegistroUsuarioView

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='usuario-registro'),
    path('perfil/', PerfilUsuarioDetailView.as_view(), name='perfil-detail'),
    path('objetivo/', ObjetivoUsuarioDetailView.as_view(), name='objetivo-detail')
]