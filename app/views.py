from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import ServicioCreateForm, FechaCreateForm
from django.urls import reverse_lazy
from .models import Lote, Servicio, Fechas


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

class FechaView(View):
    def get(self, request, *args, **kwargs):
        posts = Fechas.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'Admin/Fechas/fecha.html', context)

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
        context = {

        }
        return render(request, 'Admin/Servicios/servicios.html', context)        

class ServiciosDeleteView(DeleteView):
    model = Servicio
    template_name='Admin/Servicios/delete.html'
    success_url=reverse_lazy('Admin:servicios')

class ServiciosEditView(UpdateView):
    model=Servicio
    fields=['tipo','precio']
    template_name='Admin/Servicios/edit.html'
    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']
        return reverse_lazy('Admin:servicios')

class FechaCreateView(View):
    def get(self, request, *args, **kwargs):
        form = FechaCreateForm()
        context = {
            'form': form
        }
        return render(request, 'Admin/Fechas/create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = FechaCreateForm(request.POST)
            if form.is_valid():
                dia = form.cleaned_data.get('dia')
                hora = form.cleaned_data.get('hora')
                estado = form.cleaned_data.get('estado')

                p, created = Fechas.objects.get_or_create(dia=dia,hora=hora,estado=estado)
                p.save()
                return redirect('Admin:fecha')
        context = {

        }
        return render(request, 'Admin/Fechas/fecha.html', context)        

class FechaDeleteView(DeleteView):
    model = Fechas
    template_name='Admin/Fechas/delete.html'
    success_url=reverse_lazy('Admin:fecha')

class FechaEditView(UpdateView):
    model=Fechas
    fields=['tipo','precio']
    template_name='Admin/Fechas/edit.html'
    def get_success_url(self, **kwargs):
        pk = self.kwargs['pk']
        return reverse_lazy('Admin:fecha')
