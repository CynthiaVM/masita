from django.contrib import admin
from django.db import models
from .models import Dessert

class coreAdmin (admin.modelAdmin):
    readonly_fields= ("created","updated")

admin.site.register(Dessert, coreAdmin)


