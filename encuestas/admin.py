from encuestas.models import Encuesta, Opcion
from django.contrib import admin

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 3

class EncuestaAdmin(admin.ModelAdmin):
    campos = [
        (None,               		{'fields': ['pregunta']}),
        ('Informacion de la fecha', {'fields': ['pub_fecha'], 'classes': ['collapse']}),
    ]
    inlines = [OpcionInline]
    list_display = ('pregunta', 'pub_fecha')

admin.site.register(Encuesta, EncuestaAdmin)