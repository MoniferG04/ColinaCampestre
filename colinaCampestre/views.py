from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from app.forms import RegisterForm, ReservaForm
from app.models import Lote, Usuario, Reserva


class HomeView(View):
    def get(self, request, *args, **kwargs):
        oco01 = Lote.objects.get(id_lotes=5)
        context = {
            'oco01': oco01,
        }
        return render(request, 'index.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'about.html', context)


class ContactoView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'contacto.html', context)


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'layouts/partials/login.html', context)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm()
        if request.method == "POST":
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            try:
                usuario = Usuario.objects.get(username=request.POST['username'], password=request.POST['password'])
            except ObjectDoesNotExist:
                # manejar el caso en el que el usuario no existe
                # por ejemplo, retornar un mensaje de error
                print("error")

            
            if user is None or usuario is None:
                messages.error(request, "Credenciales incorrectas")
                return redirect('home')
            else: 
                if(usuario.estado == 'Activo'):
                    if (usuario.rol=='Administrador'): 
                        login(request,user)
                        return redirect('Admin:inicioAdmin')
                    else:
                        if (usuario.rol=="Propietario"): 
                            login(request,user)
                            return redirect('Admin:inicioDueño')
                        else:
                            login(request,user)
                            messages.success(request, "Inicio exitoso ")
                            return redirect('home')
                else:
                    messages.error(request, "Sorry, Usuario bloqueado")
                    return redirect('home')


               
            


class signoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class RegistreView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'layouts/partials/registro.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = RegisterForm(request.POST)
           # if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                # registrar usuario
                try:
                    if User.objects.filter(username=request.POST['username']).exists():
                        messages.error(request, "El usuario ya existe")
                        return redirect('home')
                    else:
                        user = User.objects.create_user(username=request.POST['username'],
                                                        email=request.POST['email'],
                                                        password=request.POST['password1'],
                                                        )
                        user.save()
                        login(request, user)
                        p, created = Usuario.objects.get_or_create(username=request.POST['username'],
                                                                email=request.POST['email'],
                                                                password=request.POST['password1'],
                                                                rol="Cliente", estado="Activo",
                                                                )
                        p.save()
                        messages.success(request, "Te has registrado correctamente")
                        return redirect('home')
                except IntegrityError:
                    messages.error(request, "Datos invalidos")
                    return redirect('home')
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('home')

            # return render(request, 'Registro.html', {
            #     'form': UserCreationForm(),
            #     "error": 'Contraseñas no coinciden'
            # })
            # return HttpResponse('Contraseñas no coinciden')
           # return render(request, 'Registro.html', {
            #        'form': UserCreationForm,
            #       "error": 'Datos invalidos'
            #   })

class InfoView(View):
    def get(self, request, id, *args, **kwargs):
        lote = Lote.objects.get(id_lotes=id)
        return render(request, 'response.html', {'lote': lote})


class error404(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'error404.html', {})
    
class ReservaView(View):
    def get(self, request, *args, **kwargs):
        post = ReservaForm()
        fechas_ocupadas = list(map(lambda x: x.strftime('%Y-%m-%d'), Reserva.objects.values_list('dia', flat=True).distinct()))
        context = {
            'post': post,
            'fechas_ocupadas': fechas_ocupadas,
        }
        
        return render(request, 'layouts/partials/reserva.html', context)
    # def post(self, request, *args, **kwargs):
    #      if request.method == "POST":
    #           form = ReservaForm(request.POST)
    #           id = request.POST.get('lote_id')
    #           if form.is_valid():
    #              dia = form.cleaned_data.get('dia')
    #              hora = form.cleaned_data.get('hora')
    #              p, created = Reserva.objects.get_or_create(dia=dia,hora=hora)
    #              p.save()
    #              lote = Lote.objects.get(id_lote=id)
    #              lote.estado = 'Reservado'
    #              lote.save()
    #              return redirect('home')
    #      return redirect('home')

