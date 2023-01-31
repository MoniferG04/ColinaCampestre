from django.urls import path
from .views import InicioUView, InicioAView, InicioDView, TerrenoView, ServiciosView, TerrenoCreateView, TerrenoEditView, TerrenoDeleteView, ServiciosCreateView, ServiciosEditView, ServiciosDeleteView

app_name="inicio"

urlpatterns  = [
    path('Cliente/', InicioUView.as_view(), name="inicioUsuario"),
    path('Admin/', InicioAView.as_view(), name="inicioAdmin"),
    path('Propietario/', InicioDView.as_view(), name="inicioDueño"),
    path('Admin/Terrenos/', TerrenoView.as_view(), name="terrenos"),
    path('Admin/Servicios/', ServiciosView.as_view(), name="servicios"),
    path('Admin/Terrenos/Crear/', TerrenoCreateView.as_view(), name="creaTerreno"),
    path('Admin/Terrenos/Editar/<int:pk>/', TerrenoEditView.as_view(), name="editaTerreno"),
    path('Admin/Terrenos/Eliminar/<int:pk>', TerrenoDeleteView.as_view(), name="eliminaTerreno"),
    path('Admin/Servicios/Crear/', ServiciosCreateView.as_view(), name="creaServicio"),
    path('Admin/Servicios/Editar/<int:pk>/', ServiciosEditView.as_view(), name="editaServicio"),
    path('Admin/Servicios/Eliminar/<int:pk>', ServiciosDeleteView.as_view(), name="eliminaServicio"),
    

]