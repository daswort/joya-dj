from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from contacto.forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email', 'noreply@example.com'),
                ['jvidal@aeurus.cl'],
            )
            return HttpResponseRedirect('general/contacto/thanks/')
    else:
        form = ContactoForm(
        	initial={'asunto': 'Me encanta este sitio.'}
        )
    return render_to_response('general/contacto.html', {'form': form})