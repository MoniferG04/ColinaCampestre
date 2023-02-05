from django.urls import path
from .views import InicioUView, InicioAView, InicioDView, TerrenoView, ServiciosView, TerrenoEditView, ServiciosCreateView, ServiciosEditView, ServiciosDeleteView, FechaView, FechaCreateView, FechaDeleteView, FechaEditView

app_name="inicio"

urlpatterns  = [
    path('Cliente/', InicioUView.as_view(), name="inicioUsuario"),
    path('Admin/', InicioAView.as_view(), name="inicioAdmin"),
    path('Propietario/', InicioDView.as_view(), name="inicioDueño"),
    path('Admin/Terrenos/', TerrenoView.as_view(), name="terrenos"),
    path('Admin/Servicios/', ServiciosView.as_view(), name="servicios"),
    path('Admin/Fechas/', FechaView.as_view(), name="fecha"),
    path('Admin/Terrenos/Editar/<int:pk>/', TerrenoEditView.as_view(), name="editaTerreno"),
    path('Admin/Servicios/Crear/', ServiciosCreateView.as_view(), name="creaServicio"),
    path('Admin/Servicios/Editar/<int:pk>/', ServiciosEditView.as_view(), name="editaServicio"),
    path('Admin/Servicios/Eliminar/<int:pk>', ServiciosDeleteView.as_view(), name="eliminaServicio"),
    path('Admin/Fechas/Crear/', FechaCreateView.as_view(), name="creaFecha"),
    path('Admin/Fechas/Editar/<int:pk>/', FechaEditView.as_view(), name="editaFecha"),
    path('Admin/Fechas/Eliminar/<int:pk>', FechaDeleteView.as_view(), name="eliminaFecha"),
    

]