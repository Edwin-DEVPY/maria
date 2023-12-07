from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.conf import settings
from django.contrib import messages

def procesar_formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        amar = request.POST.get('amar')
        apellido = request.POST.get('apellido')
        mensaje = request.POST.get('mensaje')

        if email == 'mariaangelsuarez17@gmail.com':
            enviar1(nombre=nombre,apellido=apellido,email=email,amar=amar,mensaje=mensaje)
            enviar2(nombre=nombre,apellido=apellido,email=email,amar=amar,mensaje=mensaje)
        else:
            messages.warning(request, 'Solo puede esponder esta encuensta con el corre: mariaa**********17@gmail.com')
        

    return render(request, 'index.html')


def enviar1(nombre,apellido,email,amar,mensaje):
    #mandamos un correo para verificar
            mail = 'Gracias por contestar!'
            body = render_to_string('correo.html',{
                'nombre': nombre,
                'email': email,
                'amar': amar,
                'apellido': apellido,
                'mensaje': mensaje,
            })
            user_email = email
            send_mail = EmailMessage(
                    mail,body,settings.EMAIL_HOST_USER,to=[user_email]
                )
            send_mail.from_email = False
            send_mail.send()

def enviar2(nombre,apellido,email,amar,mensaje):
    #mandamos un correo para verificar
            mail = 'Gracias por contestar!'
            body = render_to_string('correo.html',{
                'nombre': nombre,
                'email': email,
                'amar': amar,
                'apellido': apellido,
                'mensaje': mensaje,
            })
            user_email = 'monoconchudo18@gmail.com'
            send_mail = EmailMessage(
                    mail,body,settings.EMAIL_HOST_USER,to=[user_email]
                )
            send_mail.from_email = False
            send_mail.send()