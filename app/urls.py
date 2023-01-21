from django.urls import path
from .views import InicioUView, InicioAView, TerrenoView, ServiciosView, TerrenoCreateView

app_name="inicio"

urlpatterns  = [
    path('Usuario/', InicioUView.as_view(), name="inicioUsuario"),
    path('Admin/', InicioAView.as_view(), name="inicioAdmin"),
    path('Terrenos/', TerrenoView.as_view(), name="terrenos"),
    path('Servicios/', ServiciosView.as_view(), name="servicios"),
    path('Create/', TerrenoCreateView.as_view(), name="creaTerreno"),

]