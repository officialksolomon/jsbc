
from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django.core.mail import send_mail
from main.models import Contact, NewsletterSubscription
from jsbc.settings import DEFAULT_FROM_EMAIL
import logging


class Email(ModelForm):
    def new_visit_email():
        subject = "New Visitor Notification"
        message = "Someone just visited JSBC"
        recipient_list = ['ddctech.org@gmail.com', 'emenijames1@gmail.com']
        # 'emenijames1@gmail.com'
        # send email
        send_mail(subject, message,
                  DEFAULT_FROM_EMAIL, recipient_list)
