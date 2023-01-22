from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import LoteCreateForm, ServicioCreateForm
from django.urls import reverse_lazy
from .models import Lote, Servicio


class InicioAView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'Admin/home.html', context)


class ServiciosView(View):
    def get(self, request, *args, **kwargs):
        posts = Servicio.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'Admin/Servicios/servicios.html', context)


class InicioUView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'Users/home.html', context)


class TerrenoView(View):
    def get(self, request, *args, **kwargs):
        posts = Lote.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'Admin/Terrenos/terrenos.html', context)


class TerrenoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = LoteCreateForm()
        context = {
            'form': form
        }
        return render(request, 'Admin/Terrenos/create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = LoteCreateForm(request.POST)
            if form.is_valid():
                matricula = form.cleaned_data.get('matricula')
                ancho = form.cleaned_data.get('ancho')
                largo = form.cleaned_data.get('largo')
                precio = form.cleaned_data.get('precio')
                zona = form.cleaned_data.get('zona')
                estado = form.cleaned_data.get('estado')
                servicio = form.cleaned_data.get('servicio')

                p, created = Lote.objects.get_or_create(
                    ancho=ancho, largo=largo, matricula=matricula, precio=precio, zona=zona, estado=estado, servicio=servicio)
                p.save()
                return redirect('Admin:terrenos')
        context = {

        }
        return render(request, 'Admin/Terrenos/terrenos.html', context)


class TerrenoEditView(UpdateView):
    model=Lote
    fields=['ancho','largo','matricula','precio','zona','estado']
    template_name='Admin/Terrenos/edit.html'
    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']
        return reverse_lazy('Admin:terrenos')
        

class TerrenoDeleteView(DeleteView):
    model = Lote
    template_name='Admin/Terrenos/delete.html'
    success_url=reverse_lazy('Admin:terrenos')


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
        context = {

        }
        return render(request, 'Admin/Servicios/servicios.html', context)


class ServiciosEditView(UpdateView):
    model=Servicio
    fields=['tipo','precio']
    template_name='Admin/Servicios/edit.html'
    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']
        return reverse_lazy('Admin:servicios')
        

class ServiciosDeleteView(DeleteView):
    model = Servicio
    template_name='Admin/Servicios/delete.html'
    success_url=reverse_lazy('Admin:servicios')