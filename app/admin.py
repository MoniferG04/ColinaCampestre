from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register((Persona,Reserva,Lote,Factura,Servicio,Fechas))
@admin.register(Usuario)
class usuarioAdmin(admin.ModelAdmin):
    list_display=('email','password','rol',)
    list_filter=('rol',)
    search_fields=('email',)