from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    template_name = 'register.html'
    context = {
        'form': UserCreationForm()
    }
    return render(request, template_name, context)
