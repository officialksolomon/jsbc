
from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django.core.mail import send_mail
from main.models import Contact, NewsletterSubscription
from jsbc.settings import EMAIL_HOST_USER, DEFAULT_EMAIL_USERNAME
import logging


class Email(ModelForm):
    def new_visit_email():
        subject = "Contact form Notification"
        message = "Someone just visited JSBC"
        recipient_list = ['ddctech.org@gmail.com', 'emenijames1@gmail.com']
        # send email
        send_mail(subject, message,
                  DEFAULT_EMAIL_USERNAME, recipient_list)
