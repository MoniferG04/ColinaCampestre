from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import LoteCreateForm
from .models import Lote


class InicioAView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'Admin/home.html', context)


class ServiciosView(View):
    def get(self, request, *args, **kwargs):
        context = {

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

