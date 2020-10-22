from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos el correo y redireccionamos
            email = EmailMessage(
                "Multilimpio valdes: Nuevo mensaje de contacto",  
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no contestar@inbox.mailtrap.io",
                ["sebastian.retamal.ib@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #todo ha ido bien redireccionamos ha ok
                return redirect(reverse('contact')+"?ok")
            except:
                 #algo no ha ido bien redireccionamos a Fail
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
