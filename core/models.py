from django.db.models import Model, CharField, TextField, DateTimeField, ImageField

class Dessert(Model):
    title= CharField(max_length=540, verbose_name="Titulo")
    description=TextField(verbose_name= "Descripcion")
    image=ImageField(upload_to= "Dessert")
    created= DateTimeField(auto_now_add=True)
    updated= DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Postre"
        verbose_name_plural= "Postres"

    def __str__(self) -> str:
        return self.title


