from django.db import models

class Fecha(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return unicode(self.fecha.strftime("%b %d, %Y, %I:%M %p"))

class Item(models.Model):
    nombre 		= models.CharField(max_length=60)
    creado 		= models.ForeignKey(Fecha)
    prioridad 	= models.IntegerField(default=0)
    dificultad 	= models.IntegerField(default=0)
    progreso 	= models.IntegerField(default=0)
    hecho 		= models.BooleanField(default=False)

    def __unicode__(self):
        return self.nombre

    def marcar_como_hecho(self):
        return "<a href='%s'>Hecho</a>" % reverse("porHacer.views.marcar_como_hecho", args=[self.pk])
    
    marcar_como_hecho.allow_tags = True

    def progreso_(self):
    	return "<div style='width: 100px; border: 1px solid #ccc;'>" + \
      "<div style='height: 4px; width: %dpx; background: #555; '></div></div>" % self.progreso

	progreso_.allow_tags = True