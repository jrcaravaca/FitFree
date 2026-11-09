# Historial de Desarrollo y Arquitectura: FitFree

## 1. Información sobre el proyecto
- **Nombre:** FitFree (Apliación web progresiva de gestión nutricional y cambio físico)
- **Stack:**
    - **Backend:** Django, Django REST Framework, SQLite
    - **Frontend:** React + Vite, Tailwind CSS (Arquitectura PWA)
    - **Integraciones:** API Open Food Facts, API Gemini 

## 2. Registro de sesiones y progreso

- **24/10/26:** 
    -Creación de la estructura base del repositorio, configuración del enterno virtual, implementación de dependencias base e inicialización del proyecto central de Django 8 (core).
- **25/10/26:**
    -Creación de la app usuarios e inclusión en INSTALLED_APPS dentro de core/settings.py
- **31/10/26:**
    - Creación de los modelos PerfilUsuario y ObjetivoUsuario
    - Hacer migraciones de los modelos
    - Creación de la app 'alimentos' para la gestión de los alimentos
    - Creación de modelo alimento y migración. 
- 
    - Creacion de la app registros, creación de modelos Registro y Alimento consumido. 
    - Registro de modelos en admin de Django
    - Implementación de Django Rest Framework, creacion de la primera vista de la API y enlazado mediante urls.
    - Pruebas de funcionamiento
-   **09/11/26:**
    - Creada la vista 'AlimentoDetailView' basada en 'RetrieveUpdateDestroyAPIView', registrar ruta dinámica y probar respuesta buscando elementos adicionales en la API navegable de DRF
    
