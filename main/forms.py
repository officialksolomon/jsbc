
from dataclasses import field
from pyexpat import model
from django.forms import ModelForm

from main.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', "message"]


class Newsletter(ModelForm):
    class Meta:
        model = ""
        fields = ['email', ]
