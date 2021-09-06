from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

class Muffing(models.Model):
    title= models.CharField(max_length=540)
    description= models.TextField()
    image= models.ImageField(upload_to= "muffin")
    create= models.DateField(auto_now_add=True, verbose_name="fecha de crecion")
    create= models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    class Meta:
        verbose_name= "Panquesito"
        verbose_name= "Panquesitos" 

    def __str__(self):
        return self.title
