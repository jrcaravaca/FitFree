from django.urls import path
from .views import AlimentoListCreateView, AlimentoDetailView


urlpatterns = [
    path('', AlimentoListCreateView.as_view(), name='alimento-list-create'),
    path('<int:pk>/', AlimentoDetailView.as_view(), name='alimento-detail')
]

