# Historial de Desarrollo y Arquitectura: FitFree

## 1. Información sobre el proyecto
- **Nombre:** FitFree (Apliación web progresiva de gestión nutricional y cambio físico)
- **Stack:**
    - **Backend:** Django, Django REST Framework, SQLite
    - **Frontend:** React + Vite, Tailwind CSS (Arquitectura PWA)
    - **Integraciones:** API Open Food Facts, API Gemini 

## 2. Registro de sesiones y progreso

- 24/10/26: Creación de la estructura base del repositorio, configuración del enterno virtual, implementación de dependencias base e inicialización del proyecto central de Django 8 (core).
- 25/10/26: Creación de la app usuarios e inclusión en INSTALLED_APPS dentro de core/settings.py
- 31/10/26: Creación de los modelos PerfilUsuario y ObjetivoUsuario; Hacer migraciones de los modelos; Creación de la app 'alimentos' para la gestión de los alimentos; Creación de modelo alimento y migración. 