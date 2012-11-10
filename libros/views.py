from django.http import HttpResponse
from django.shortcuts import render_to_response
from libros.models import Libro

def buscador(request):
	errors = []
	q = None;
	if 'q' in request.GET:
		q = request.GET['q']
    	if not q:
            errors.append('Por favor ingrese un termino de busqueda.')
        elif len(q) > 20:
            errors.append('No puede ingresar mas de 20 caracteres.')
        else:
    		libros = Libro.objects.filter(titulo__icontains=q)
        	return render_to_response('libros/resultado_busqueda.html', {'libros': libros, 'query': q})
	return render_to_response('libros/buscador.html', {'errors': errors})