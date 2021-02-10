from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContacForm

# Create your views here.
def contact(request):
    contact_form= ContacForm()

    if request.method=="POST" :
        contact_form= ContacForm(data= request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            #we suppose everythings went right
            # we send the message and we redirect it
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", #subject
                "De {} <{}> \n\n Escribio: \n\n {}".format(name, email, content), #body
                "no-contestar@inbox.mailtrap.io", #email_origen
                ["suyon.jesus@gmail.com"], #email_to
                reply_to = [email], #reply_to
            )

            # funtion to send the email
            try:
                #if all is right the email will be sent
                email.send()
                return redirect(reverse('contact')+"?ok")

            except:
                # if something occur or happend , we redirect to FAIL
                return redirect(reverse('contact')+"?fail")



    return render(request, 'contact/contact.html', {'form':contact_form})