from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

def enviar_email_bem_vindo_basico(usuario_email, nome_usuario):
    send_mail(
        "Bem vindo!",
        f"Seja muito bem vindo(a) {nome_usuario} ao nosso site! O melhor e mais completo de todos.",
        settings.EMAIL_HOST_USER,
        [usuario_email],
        fail_silently=False,
    )

def enviar_email_bem_vindo_avancado(usuario_email, nome_usuario):
    txt_content = render_to_string('emails/bem_vindo/email_template.txt', {'nome': nome_usuario})
    html_content = render_to_string('emails/bem_vindo/email_template.html', {'nome': nome_usuario})
    msg = EmailMultiAlternatives(
        "Bem vindo!",
        txt_content,
        settings.EMAIL_HOST_USER,
        [usuario_email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()