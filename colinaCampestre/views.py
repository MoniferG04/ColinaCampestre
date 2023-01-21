from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'index.html', context)

class LoginView(View):
     def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        context={
            'form':form
        }
        return render(request, 'login.html', context)
     def post(self, request, *args, **kwargs):
        if request.method == "POST":
            if request.POST['password1'] == request.POST['password2']:
                #registrar usuario
                try:
                    user =  User.objects.create_user(username=request.POST['username'],
                    password=request.POST['password1'])
                    user.save()
                    return redirect('Admin:inicioAdmin')
                except:
                    return render(request, 'login.html', {
                        'form':UserCreationForm,
                        "error": 'Usuario ya existe'
                    })
                    #return HttpResponse('Usuario ya existe')

            return render(request, 'login.html', {
                        'form':UserCreationForm,
                        "error": 'Contraseñas no coinciden'
                    })
            # return HttpResponse('Contraseñas no coinciden')

