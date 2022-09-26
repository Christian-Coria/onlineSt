from django.db import models


class Formato(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
       return f'{self.tipo}'


class Interprete(models.Model):
    nombre = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="caratula", null=True, blank=True)

    def __unicode__(self): 
        return f'{self.nombre}'

    class Meta:
        ordering = ['-nombre']

    def __str__(self):
      return f'{self.nombre}'

    
class Genero(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
      return f'{self.nombre}'


class Discografica(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
       return f'{self.nombre}'


class Album(models.Model):

    nombre = models.CharField(max_length=255)
    interprete = models.ForeignKey(Interprete,null=True, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,null=True, on_delete=models.CASCADE)
    cant_temas = models.CharField(max_length=40)
    discografica = models.ForeignKey(Discografica,null=True, on_delete=models.CASCADE)
    formato = models.ForeignKey(Formato,null=True, on_delete=models.CASCADE)
    fec_lanzamiento = models.CharField(max_length=40)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(upload_to="caratula", null=True, blank=True)
  
    def __str__(self):
       return f'{self.nombre}'


class Tema(models.Model):
    titulo = models.CharField(max_length=255)
    duracion = models.IntegerField()
    autor = models.CharField(max_length=255)
    compositor = models.CharField(max_length=255)
    cod_album = models.ForeignKey(Album,null=True, on_delete=models.CASCADE)
    interprete = models.ForeignKey(Interprete,null=True, on_delete=models.CASCADE)

    def __str__(self):
      return f'{self.titulo}' 