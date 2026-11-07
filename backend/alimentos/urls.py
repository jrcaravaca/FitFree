from django.urls import path
from .views import AlimentoListCreateView


urlpatterns = [
    path('', AlimentoListCreateView.as_view(), name='alimento-list-create'),
]