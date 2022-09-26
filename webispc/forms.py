from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormatoCreationForm(forms.Form):
    tipo = forms.CharField(max_length=40)

    
class InterpreteCreationForm(forms.Form):
    nombre = forms.CharField(max_length=255)
    foto = forms.ImageField(upload_to="caratula", null=True, blank=True)

    
class GeneroCreationForm(forms.Form):
    nombre = forms.CharField(max_length=255)

    
class DiscograficaCreationForm(forms.Form):
    nombre = forms.CharField(max_length=50)

    
class TemaCreationForm(forms.Form):
    titulo = forms.CharField(max_length=255)
    duracion = forms.IntegerField()
    autor = forms.CharField(max_length=255)
    compositor = forms.CharField(max_length=255)
    cod_album = forms.ForeignKey(Album,null=True, on_delete=forms.CASCADE)
    interprete = forms.CharField(max_length=255)

    
class AlbumCreationForm(forms.Form):                   

    nombre = forms.CharField(label='Nombre', max_length=30, required=False)
    interprete = forms.ForeignKey(Interprete, on_delete=forms.DO_NOTHING)
    genero = forms.ForeignKey(Genero, on_delete=forms.DO_NOTHING)
    cant_temas = forms.CharField(label='Cantidad de Temas', widget=forms.PasswordInput,required=False)
    discografica = forms.ForeignKey(Discografica, on_delete=forms.DO_NOTHING)
    fec_lanzamiento = forms.CharField(max_length=40)
    precio = forms.IntegerField()    
    cantidad = forms.IntegerField()

    