from .views import HomeView, RegistreView, LoginView, signoutView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('',include('app.urls', namespace='Users')),
    path('',include('app.urls', namespace='Admin')),
    path('Login/', LoginView.as_view(), name="login"),
    path('Registro/', RegistreView.as_view(), name="Registro"),
    path('Logout',signoutView.as_view(), name="Cerrar"),



]

