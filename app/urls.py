from django.urls import path
from .views import *
from . import views

app_name="inicio"

urlpatterns  = [
    path('Cliente/', InicioUView.as_view(), name="inicioUsuario"),
    path('Admin/', InicioAView.as_view(), name="inicioAdmin"),
    path('Propietario/', InicioDView.as_view(), name="inicioDueño"),
    path('Admin/Terrenos/', TerrenoView.as_view(), name="terrenos"),
    path('Admin/Servicios/', ServiciosView.as_view(), name="servicios"),
    path('Admin/Reservaciones/', ReservacionView.as_view(), name="Reserva"),
    path('Admin/Usuarios/', UsuariosView.as_view(), name="usuario"),
    path('Admin/Reservaciones/vendido/<int:pk>', CambiarAEstadoVendidoView.as_view(), name='lote_vendido'),
    path('Admin/Reservaciones/disponible/<int:pk>', CambiarAEstadoDisponibleView.as_view(), name='lote_disponible'),
    path('Admin/Terrenos/Editar/<int:pk>/', TerrenoEditView.as_view(), name="editaTerreno"),
    path('Admin/Servicios/Crear/', ServiciosCreateView.as_view(), name="creaServicio"),
    path('Admin/Servicios/Editar/<int:pk>/', ServiciosEditView.as_view(), name="editaServicio"),
    path('Admin/Servicios/eliminar/<int:id>', views.eliminar_servicio, name="eliminar_servicio"),
    path('Admin/Usuarios/Crear/', UsuarioCreateView.as_view(), name="creaUsuario"),
    path('Admin/Usuarios/Editar/<int:pk>/', UsuarioEditView.as_view(), name="editaUsuario"),
    path('Admin/Usuarios/eliminar/<int:id>', views.eliminar_usuario, name="eliminar_usuario"),

]