from django.shortcuts import render
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
