from .views import HomeView, RegistreView, LoginView, signoutView, AboutView, ContactoView, InfoView, error404, ReservaView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('',include('app.urls', namespace='Users')),
    path('',include('app.urls', namespace='Admin')),
    path('Login/', LoginView.as_view(), name="login"),
    path('Registro/', RegistreView.as_view(), name="Registro"),
    path('Logout/',signoutView.as_view(), name="Cerrar"),
    path('about/', AboutView.as_view(), name='about'),
    path('contacto/',ContactoView.as_view(), name='contacto'),
    path('info/<int:id>',InfoView.as_view(), name='info'),
    path('Reserva/', ReservaView.as_view(), name="reserva"),


]

handler404 =  error404.as_view()
