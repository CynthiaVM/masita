from django.shortcuts import render
from django.http import response
from .models import Dessert


def home(request):
    postrecitos= Dessert.objects.all()
    return render(request, 'core/index.html', {"postres": postrecitos})
    