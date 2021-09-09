from django.db import models, charfield
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField
 
class Dessert(Model):
    title= CharField (max_length=540, verbose_name= "Titulo")
    description= TextField(verbose_name= "Descripcion")
    image= models.ImageField(upload_to= "dessert")
    create= models.DateField(auto_now_add=True)
    create= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Postre"
        verbose_name= "Postres" 

    def __str__(self):
        return self.title

