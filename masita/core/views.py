from django.shortcuts import render
from .models import Dessert


def home(request):
    postrecitos= Dessert.objects.all()
    return render(request, "core/index.html", {"postres": postrecitos})
    