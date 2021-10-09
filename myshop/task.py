# from Celery import task
from django.core.mail import send_mail
from .models import *
from celery import shared_task
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags

# from demoapp.models import Widget
from projectshop.settings import EMAIL_HOST_USER
@shared_task
def ordrt_email_send(order_id,email):
    title="Marazzodan salom!"
    html_message = render_to_string('mail_template.html',{'context': Orders.objects.get(id=order_id).orderitm.all()})
    # return render(request,'mail_template.html',{'context': orders.orderitm.all()})

    plain_message = strip_tags(html_message)

    send_mail(title, plain_message, EMAIL_HOST_USER,[email,email,email,email,email,email,
    email,email,email,email,email,email,email,email], html_message=html_message)


# @shared_task
# def add(x, y):
#     return x + y


# @shared_task
# def mul(x, y):
#     return x * y


# @shared_task
# def xsum(numbers):
#     return sum(numbers)


# @shared_task
# def count_widgets():
#     return Widget.objects.count()


# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()