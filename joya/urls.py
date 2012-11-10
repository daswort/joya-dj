from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from encuestas.models import Encuesta
from libros.models import Libro
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^libros/buscador/$', 'libros.views.buscador'),
	#(r'^libros/buscar/$', 'libros.views.buscar'),
	(r'^contacto/$', 'contacto.views.contacto'),
    (r"^marcar_como_hecho/(\d*)/$", 'porHacer.views.marcar_como_hecho'),
    # Examples:
    # url(r'^$', 'joya.views.home', name='home'),
    # url(r'^joya/', include('joya.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
