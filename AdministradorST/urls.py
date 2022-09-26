from django.urls import path
from integrador.views import (ProyectoIntegrador, ProyectoIntegrador, CrearFormato, EliminarFormato, EditarFormato, ListarFormato ,MostrarFormato,
CrearAlbum, EliminarAlbum ,EditarAlbum , ListarAlbum, MostrarAlbum, CrearTema, EliminarTema, EditarTema, ListarTema, MostrarTema, 
CrearInterprete, EliminarInterprete, EditarInterprete, ListarInterprete, CrearGenero, MostrarInterprete, EliminarGenero, EditarGenero, MostrarGenero ,ListarGenero,
CrearDiscografica,  EliminarDiscografica, EditarDiscografica, ListarDiscografica,  MostrarDiscografica )


urlpatterns = [
    
    path('proyecto',ProyectoIntegrador.as_view(), name="proyecto"),         
   
    path('crear-formato' , CrearFormato.as_view(), name='crear_formato'),        
    path('eliminar-formato/<int:pk>' , EliminarFormato.as_view(), name='eliminar_formato'),
    path('editar-formato/<int:pk>' , EditarFormato.as_view(), name='editar_formato'),
    path('listar-formato' , ListarFormato.as_view(), name='listar_formato'),
    path('mostrar-formato/<int:pk>/' , MostrarFormato.as_view(), name='mostrar_formato'),

    path('crear-album' , CrearAlbum.as_view(), name='crear_album'),
    path('eliminar-album/<int:pk>' , EliminarAlbum.as_view(), name='eliminar_album'),
    path('editar-album/<int:pk>' , EditarAlbum.as_view(), name='editar_album'),
    path('listar-album' , ListarAlbum.as_view(), name='listar_album'),
    path('mostrar-album/<int:pk>/' , MostrarAlbum.as_view(), name='mostrar_album'),

    path('crear-tema' , CrearTema.as_view(), name='crear_tema'),
    path('eliminar-tema/<int:pk>' , EliminarTema.as_view(), name='eliminar_tema'),
    path('editar-tema/<int:pk>' , EditarTema.as_view(), name='editar_tema'),
    path('listar-tema' , ListarTema.as_view(), name='listar_tema'),
    path('mostrar-tema/<int:pk>/' , MostrarTema.as_view(), name='mostrar_tema'),

    path('crear-interprete' , CrearInterprete.as_view(), name='crear_interprete'),
    path('eliminar-interprete/<int:pk>' , EliminarInterprete.as_view(), name='eliminar_interprete'),
    path('editar-interprete/<int:pk>' , EditarInterprete.as_view(), name='editar_interprete'),
    path('listar-interprete' , ListarInterprete.as_view(), name='listar_interprete'),
    path('mostrar-interprete/<int:pk>/' , MostrarInterprete.as_view(), name='mostrar_interprete'),

    path('crear-genero' , CrearGenero.as_view(), name='crear_genero'),
    path('eliminar-genero/<int:pk>' , EliminarGenero.as_view(), name='eliminar_genero'),
    path('editar-genero/<int:pk>' , EditarGenero.as_view(), name='editar_genero'),
    path('listar-genero' , ListarGenero.as_view(), name='listar_genero'),
    path('mostrar-genero/<int:pk>/' , MostrarGenero.as_view(), name='mostrar_genero'),

    path('crear-discografica' , CrearDiscografica.as_view(), name='crear_discografica'),
    path('eliminar-discografica/<int:pk>' , EliminarDiscografica.as_view(), name='eliminar_discografica'),
    path('editar-discografica/<int:pk>' , EditarDiscografica.as_view(), name='editar_discografica'),
    path('listar-discografica' , ListarDiscografica.as_view(), name='listar_discografica'),
    path('mostrar-discografica/<int:pk>/' , MostrarDiscografica.as_view(), name='mostrar_discografica'),

]