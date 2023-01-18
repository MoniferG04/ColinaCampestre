from django.views.generic import View
from django.shortcuts import render

class LoginView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'login.html', context)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'index.html', context)