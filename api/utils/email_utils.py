<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 040cc708bb4ba6673971516f48508dacf2e5fe5b
from django.core.mail import send_mail
from django.conf import settings

def enviar_correo(destinatario, asunto, mensaje):
    """Envía un correo electrónico"""
    try:
        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[destinatario],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error al enviar correo: {e}")
<<<<<<< HEAD
=======
from django.core.mail import send_mail
from django.conf import settings

def enviar_correo(destinatario, asunto, mensaje):
    """Envía un correo electrónico"""
    try:
        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[destinatario],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error al enviar correo: {e}")
>>>>>>> bc835c3 (Subo cambios de pruebas y ajustes)
=======
>>>>>>> 040cc708bb4ba6673971516f48508dacf2e5fe5b
        return False