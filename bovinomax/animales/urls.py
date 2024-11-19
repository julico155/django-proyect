from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_animales, name='listar_animales'),
    path('crear/', views.crear_animal, name='crear_animal'),
    path('editar/<int:id>/', views.editar_animal, name='editar_animal'),
    path('eliminar/<int:id>/', views.eliminar_animal, name='eliminar_animal'),
]
