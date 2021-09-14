from django.db.models import Model, CharField, TextField, DateTimeField, ImageField

class Dessert(Model):
    title= CharField(max_length=540, verbose_name="Titulo")
    description=TextField(verbose_name= "Descripcion")
    image=ImageField(upload_to= "Dessert")
    create= DateTimeField(auto_now_add=True)
    create= DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Postre"
        verbose_name= "Postres" 

    def __str__(self) -> str:
        return self.title


