
from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django.core.mail import send_mail
from main.models import Contact, NewsletterSubscription
from jsbc.settings import EMAIL_HOST_USER
import logging

class ContactForm(ModelForm):

    def send_mail(self):
        admin_subject = "Contact form Notification"
        user_subject = "JSBC Support"
        admin_message = self.cleaned_data['message']
        user_message = "Thank you for taking out time to reachout to us. We would respond to you shortly"
        user_email = self.cleaned_data['email']
        recipient_list = ['ddctech.org@gmail.com', EMAIL_HOST_USER]
        # admin
        send_mail(admin_subject, admin_message,
                  EMAIL_HOST_USER, recipient_list, fail_silently=True)
        # user
        send_mail(user_subject, user_message, EMAIL_HOST_USER, [user_email], fail_silently=True)


    class Meta:
        model = Contact
        fields = ['name', 'email', "message"]


class NewsletterForm(ModelForm):
    def send_mail(self):
        admin_subject = "Newsletter Subcription Notification"
        admin_message = f"New User with E-main address {self.cleaned_data['email']} susbcribed to our newsletter."
        recipient_list = ['ddctech.org@gmail.com']
        # admin
        send_mail(admin_subject, admin_message, EMAIL_HOST_USER,
                  recipient_list, fail_silently=True)

    class Meta:
        model = NewsletterSubscription
        fields = ['email', ]
