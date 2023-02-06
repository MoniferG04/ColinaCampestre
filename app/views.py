from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import ServicioCreateForm, UsuarioCreateForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Lote, Servicio, Reserva, Usuario


class InicioAView(View):
    def get(self, request, *args, **kwargs):
        oco01 = Lote.objects.get(id_lotes=5)
        context = {
        'oco01': oco01,
        }
        return render(request, 'Admin/home.html', context)


class ServiciosView(View):
    def get(self, request, *args, **kwargs):
        posts = Servicio.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'Admin/Servicios/servicios.html', context)

class UsuariosView(View):
    def get(self, request, *args, **kwargs):
        posts = Usuario.objects.filter(rol__in=['Cliente', 'Propietario'])
        context = {
            'posts': posts
        }
        return render(request, 'Admin/Usuarios/usuarios.html', context)

class ReservacionView(View):
    def get(self, request, *args, **kwargs):
        posts = Reserva.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'Admin/Reservaciones/Reservaciones.html', context)

class InicioDView(View):
    def get(self, request, *args, **kwargs):
        posts = Servicio.objects.all()
        context = {
            'posts':posts
        }
        return render(request, 'Users/Dueño/home.html', context)

class InicioUView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'Users/Cliente/home.html', context)


class TerrenoView(View):
    def get(self, request, *args, **kwargs):
        oco01 = Lote.objects.get(id_lotes=5)
        context = {
            'oco01': oco01,
        }
        return render(request, 'Admin/Terrenos/terrenos.html', context)

class TerrenoEditView(UpdateView):
    model=Lote
    fields=['ancho','largo','matricula','precio','zona','estado']
    template_name='Admin/Terrenos/edit.html'
    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']

        return reverse_lazy('Admin:terrenos')

class ServiciosCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ServicioCreateForm()
        context = {
            'form': form
        }
        return render(request, 'Admin/Servicios/create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ServicioCreateForm(request.POST)
            if form.is_valid():
                tipo = form.cleaned_data.get('tipo')
                
                precio = form.cleaned_data.get('precio')
                

                p, created = Servicio.objects.get_or_create(tipo=tipo, precio=precio)
                p.save()
                return redirect('Admin:servicios')
            
        return redirect('Admin:servicios')      


def eliminar_servicio(request,id):
    servicio = Servicio.objects.get(id_servicio=id)
    servicio.delete()
    return redirect(to='Admin:servicios')
    

class ServiciosEditView(UpdateView):
    model=Servicio
    fields=['tipo','precio']
    template_name='Admin/Servicios/edit.html'
    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']
        return reverse_lazy('Admin:servicios')

class CambiarAEstadoVendidoView(View):
    def get(self, request, *args, **kwargs):
        lote = get_object_or_404(Lote, matricula=kwargs['pk'])
        lote.estado = "Vendido"
        lote.save()
        return redirect('Admin:terrenos')

class CambiarAEstadoDisponibleView(View):
    def get(self, request, *args, **kwargs):
        lote = get_object_or_404(Lote, matricula=kwargs['pk'])
        lote.estado = "Disponible"
        lote.save()
        return redirect('Admin:terrenos')

class UsuarioCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UsuarioCreateForm()
        context = {
            'form': form
        }
        return render(request, 'Admin/Usuarios/create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = UsuarioCreateForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                estado = "Activo"
                rol="Propietario"
                
                user = User.objects.create_user(username=username,
                                                                email=email,
                                                                password=password,
                                                        )
                user.save()
                p, created = Usuario.objects.get_or_create(username=username,
                                                                email=email,
                                                                password=password,
                                                                rol=rol, estado=estado,
                                                                )
                p.save()
                return redirect('Admin:usuario')
        return redirect('Admin:usuario')       

def eliminar_usuario(request,id):
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect(to='Admin:usuario')
    

class UsuarioEditView(UpdateView):
    model=Usuario
    fields=['username','email','password','rol','estado']
    template_name='Admin/Usuarios/edit.html'
    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']
        return reverse_lazy('Admin:usuario')