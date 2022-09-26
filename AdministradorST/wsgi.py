from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView, DetailView, TemplateView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from integrador.models import  Formato, Album, Discografica, Genero, Interprete, Tema

class ProyectoIntegrador(TemplateView):
    template_name = "integrador/proyecto.html"


def buscar_album(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_album_list = Album.objects.filter(Q(nombre__icontains=q)).order_by('nombre',
        Q(genero__icontains=q)).order_by('genero'), (Q(interprete__icontains=q)).order_by('interprete')
    else:
        all_album_list = Album.objects.all().order_by('nombre')
        all_album_list = Album.objects.all().order_by('genero')
        all_album_list = Album.objects.all().order_by('interprete')

    return render(request, 'buscar_album.html', {"album":all_album_list})


class CrearAlbum(CreateView):        
    model = Album
    template_name = "integrador/crear_album.html"
    success_url = 'proyecto'
    fields = ['nombre','interprete','genero','cant_temas', 'discografica', 'formato', 'fec_lanzamiento', 'precio', 'cantidad']


class ListarAlbum(ListView):
    model = Album
    template_name = "integrador/listar_album.html"


class EditarAlbum(UpdateView):
    model = Album
    template_name ='integrador/editar_album.html'
    success_url = reverse_lazy('listar_albums')
    fields = ['nombre','interprete','genero','cant_temas', 'discografica', 'formato', 'fec_lanzamiento', 'precio', 'cantidad'] 


class EliminarAlbum(DeleteView):
    model = Album
    template_name = "integrador/eliminar_album.html"
    success_url = reverse_lazy('listar_album')


class MostrarAlbum(DetailView):
    model = Album
    template_name = 'integrador/mostrar_album.html'

class CrearFormato(CreateView):
    model = Formato
    template_name = "integrador/crear_formato.html"
    success_url = 'proyecto'
    fields = ['tipo']


class ListarFormato(ListView):
    model = Formato
    template_name = "integrador/listar_formato.html"


class EditarFormato(UpdateView):
    model = Formato
    template_name ='integrador/editar_formato.html'
    success_url = reverse_lazy('listar_formato')
    fields = ['tipo'] 


class EliminarFormato(DeleteView):
    model =  Formato
    template_name = "integrador/eliminar_formato.html"
    success_url = reverse_lazy('listar_formato')


class MostrarFormato(DetailView):
    model = Formato
    template_name = 'integrador/mostrar_formato.html'


class CrearTema(CreateView):        
    model = Tema
    template_name = "integrador/crear_tema.html"
    success_url = 'proyecto'
    fields = ['titulo','duracion','autor','compositor', 'cod_album', 'interprete']


class ListarTema(ListView):
    model = Tema
    template_name = "integrador/listar_tema.html"


class EditarTema(UpdateView):
    model = Tema
    template_name ='integrador/editar_tema.html'
    success_url = reverse_lazy('listar_tema')
    fields = ['titulo','duracion','autor','compositor', 'cod_album', 'interprete'] 


class EliminarTema(DeleteView):
    model = Tema
    template_name = "integrador/eliminar_tema.html"
    success_url = reverse_lazy('listar_tema')


class MostrarTema(DetailView):
    model = Tema
    template_name = 'mostrar_tema.html'


class CrearInterprete(CreateView):        
    model = Interprete
    template_name = "integrador/crear_interprete.html"
    success_url = 'proyecto'
    fields = ['nombre', 'foto']


class ListarInterprete(ListView):
    model = Interprete
    template_name = "integrador/listar_interprete.html"


class EditarInterprete(UpdateView):
    model = Interprete
    template_name ='integrador/editar_interprete.html'
    success_url = reverse_lazy('listar_interprete')
    fields = ['nombre', 'foto'] 


class EliminarInterprete(DeleteView):
    model = Interprete
    template_name = "integrador/eliminar_interprete.html"
    success_url = reverse_lazy('listar_interprete')


class MostrarInterprete(DetailView):
    model = Interprete
    template_name = 'integrador/mostrar_interprete.html'


class CrearGenero(CreateView):        
    model = Genero
    template_name = "integrador/crear_genero.html"
    success_url = 'proyecto'
    fields = ['nombre']


class ListarGenero(ListView):
    model = Genero
    template_name = "integrador/listar_genero.html"


class EditarGenero(UpdateView):
    model = Genero
    template_name ='integrador/editar_genero.html'
    success_url = reverse_lazy('listar_genero')
    fields = ['nombre'] 


class EliminarGenero(DeleteView):
    model = Genero
    template_name = "integrador/eliminar_genero.html"
    success_url = reverse_lazy('listar_genero')


class MostrarGenero(DetailView):
    model = Genero
    template_name = 'integrador/mostrar_genero.html'


class CrearDiscografica(CreateView):        
    model = Discografica
    template_name = "integrador/crear_discografica.html"
    success_url = 'proyecto'
    fields = ['nombre']


class ListarDiscografica(ListView):
    model = Discografica
    template_name = "integrador/listar_discografica.html"


class EditarDiscografica(UpdateView):
    model = Discografica
    template_name ='integrador/editar_discografica.html'
    success_url = reverse_lazy('listar_discografica')
    fields = ['nombre'] 


class EliminarDiscografica(DeleteView):
    model = Discografica
    template_name = "integrador/eliminar_discografica.html"
    success_url = reverse_lazy('listar_discografica')


class MostrarDiscografica(DetailView):
    model = Discografica
    template_name = 'integrador/mostrar_discografica.html'
