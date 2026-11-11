from django.urls import path
from .views import (
    RegistroListCreateView,
    RegistroDetailView,
    AlimentoConsumidoCreateView,
    AlimentoConsumidoDetailView
) 

urlpatterns = [
    path('', RegistroListCreateView.as_view(), name='registro-list-create'),
    path('<int:pk>/', RegistroDetailView.as_view(), name='registro-detail'), 
    path('item/', AlimentoConsumidoCreateView.as_view(), name='alimento-consumido-create'),
    path('item/<int:pk>/', AlimentoConsumidoDetailView.as_view(), name='alimento-consumido-detail'),
]