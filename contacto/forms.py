from django import forms

class ContactoForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='e-mail')
    mensaje = forms.CharField(widget=forms.Textarea)

    def limpiar_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError("No hay suficientes palabras!")
        return mensaje