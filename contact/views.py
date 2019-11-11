from django.shortcuts import render, redirect
# Importamos la librería de email message:
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm

def contact(request):
    print("Tipo de petición: {}".format(request.method)) 

    contact_form = ContactForm() 

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Ahora a la variable email le pasamos el EmailMessage con los datos del correo:
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", # Este es el asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content), # este es el cuerpo
                "no-contestar@inbox.mailtrap.io", # Este sería el email de origen que lo definimos como un no-contestar
                ["guilelrmogranadosgomez@gmail.com"], # Estos son los email de destino que recibirán el mensaje del formulario
                reply_to=[email] # Este es el email del cliente
            )
            # enviamos el email capturando cualquier error:
            try:
                email.send()
                return redirect(reverse('contact')+'?ok') 
            except:
                return redirect(reverse('contact')+'?fall') # Retornamos al formulario con un parametro de fallo

    return render(request, 'contact/contact.html', {'form': contact_form})