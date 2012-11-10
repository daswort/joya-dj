from django.db import models

class Encuesta(models.Model):
    pregunta = models.CharField(max_length=200)
    pub_fecha = models.DateTimeField('date published')

    def __unicode__(self):
        return self.pregunta

    def fue_publicado_recien(self):
        return self.pub_fecha >= timezone.now() - datetime.timedelta(days=1)

class Opcion(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    opcion = models.CharField(max_length=200)
    votos = models.IntegerField()

    def __unicode__(self):
        return self.opcion
