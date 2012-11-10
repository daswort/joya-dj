from django.db import models

class Editor(models.Model):
    nombre 		= models.CharField(max_length=30)
    direccion 	= models.CharField(max_length=50)
    ciudad 		= models.CharField(max_length=60)
    region 		= models.CharField(max_length=30)
    pais 		= models.CharField(max_length=50)
    website 	= models.URLField()

    def __unicode__(self):
        return self.nombre

class Autor(models.Model):
    nombre 		= models.CharField(max_length=30)
    apellido 	= models.CharField(max_length=40)
    email 		= models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.apellido)

class Libro(models.Model):
    titulo 				= models.CharField(max_length=100)
    autores 			= models.ManyToManyField(Autor)
    editor 				= models.ForeignKey(Editor)
    fecha_publicacion 	= models.DateField()

    def __unicode__(self):
        return self.titulo