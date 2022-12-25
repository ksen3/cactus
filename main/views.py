from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *


def index(request):
    mainCards = MainContent.objects.all()
    context = {
        'mainCards': mainCards,
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print('form is not valid')
    else:
        form = ReviewForm()


    context = {'form': form, }
    return render(request, 'main/contacts.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('login')
