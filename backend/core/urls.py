from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alimentos/', include('alimentos.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/registros/', include('registros.urls'))
]
