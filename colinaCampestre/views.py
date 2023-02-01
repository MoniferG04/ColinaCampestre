from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from app.forms import RegisterForm
from app.models import Lote


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

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
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm()
        if request.method == "POST":
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                context = {
                    'form': form,
                    'error': 'usuario o contraseña incorrectas'
                  }
                return render(request, 'login.html', context)
            else: 
                if (request.POST['username']=='ColinaCampestre'): 
                    login(request,user)
                    return redirect('Admin:inicioAdmin')
                else:
                    if (request.POST['username']=='FreinderMatoma'): 
                        login(request,user)
                        return redirect('Admin:inicioDueño')
                    else:
                        login(request,user)
                        return redirect('Admin:inicioUsuario')
           
class signoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class RegistreView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm
        context = {
            'form': form
        }
        return render(request, 'Registro.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = RegisterForm(request.POST)
           # if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                # registrar usuario
                try:
                    user = User.objects.create_user(username=request.POST['username'],
                                                    email=request.POST['email'],
                                                    password=request.POST['password1'],
                                                    )
                    user.save()
                    # p.save()
                    login(request, user)
                    return redirect('Admin:inicioAdmin')
                except IntegrityError:
                    return render(request, 'Registro.html', {
                        'form': UserCreationForm,
                        "error": 'Usuario ya existe'
                    })
                    # return HttpResponse('Usuario ya existe')

            return render(request, 'Registro.html', {
                'form': UserCreationForm,
                "error": 'Contraseñas no coinciden'
            })
            # return HttpResponse('Contraseñas no coinciden')
           # return render(request, 'Registro.html', {
            #        'form': UserCreationForm,
            #       "error": 'Datos invalidos'
            #   })

class InfoView(View):
    def get(self,request, id ,*args, **kwargs):
        try:
            lote = Lote.objects.get(id_lotes=id)
        except:
            lote=Lote()
        return render(request, 'response.html',{'lote':lote})

class error404(View):
    def get(self, request, *args, **kwargs):
        return render(request,'error404.html',{})

