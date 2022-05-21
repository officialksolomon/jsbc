
from dataclasses import field
from pyexpat import model
from django.forms import ModelForm

from main.models import Contact, NewsletterSubscription


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', "message"]


class NewsletterForm(ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email', ]
