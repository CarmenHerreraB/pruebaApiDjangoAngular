from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter #router para registrar las rutas automáticamente
from .views import StudentViewSet

# 1. Crear el router
router =DefaultRouter()

# 2. Registrar el ViewSet en el router
router.register (r'students', StudentViewSet) #CLASE DESDE EL ARCIVO VIEWS  con viewsets-  - Y CRUD - GET, POST ,PUT , PATCH, DELETE


urlpatterns = [
    path('', include(router.urls)),    # <-- Aquí registras las rutas  (GET -POST ) 
]