from django.urls import path
from .views import ListarLaboratorio, CrearLaboratorio, EditarLaboratorio, EliminarLaboratorio, DetalleLaboratorio

urlpatterns = [
    path('', ListarLaboratorio.as_view(), name='laboratorios'),
    path('crear/', CrearLaboratorio.as_view(), name='crear-laboratorio'),
    path('editar/<int:pk>/', EditarLaboratorio.as_view(), name='editar-laboratorio'),
    path('<int:pk>/', DetalleLaboratorio.as_view(), name='detalle'),
    path('eliminar/<int:pk>/', EliminarLaboratorio.as_view(), name='eliminar-laboratorio'),
]