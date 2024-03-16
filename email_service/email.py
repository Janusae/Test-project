from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def Send_gmail(subject , to , context , template ):
    try:
        html = render_to_string(template, context)
        plain_text = strip_tags(html)
        who = settings.EMAIL_HOST_USER
        send_mail(subject , plain_text ,who, [to], html_message=html)
    except Exception as e:
        print(e)