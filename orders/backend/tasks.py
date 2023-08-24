from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def reset_password_token_created_msg_send(msg):
    msg.send()

@shared_task()
def new_user_registered_signal_msg_send(msg):
    msg.send()


@shared_task()
def new_order_signal_msg_send_msg_send(msg):
    msg.send()
