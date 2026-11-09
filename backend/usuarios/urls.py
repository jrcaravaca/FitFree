from django.urls import path
from .views import PerfilUsuarioDetailView, ObjetivoUsuarioDetailView

urlpatterns = [
    path('perfil/<int:pk>/', PerfilUsuarioDetailView.as_view(), name=('perfil-detail')),
    path('objetivo/<int:pk>/', ObjetivoUsuarioDetailView.as_view(), name=('objetivo-detail'))
]