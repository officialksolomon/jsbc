

from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from main.models import Contact, NewsletterSubscription, Profile
from jsbc.settings import EMAIL_HOST_USER, DEFAULT_FROM_EMAIL
from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    terms_consent = forms.BooleanField(
        required=True, initial=False,  label='I have read and consent to the terms and conditions?')
    field_order = ['username', 'email',
                   'password1', 'password2', 'terms_consent', ]

    def save(self, request):
        # Ensure you call the parent class's save.
        user = super(CustomSignupForm, self).save(request)

        # create profile and save consent
        Profile.objects.create(user=user, terms_consent=True)

        # You must return the original result.
        return user


field_order = ['username', 'email',
               'password1', 'password2', 'terms_consent', ]


class ContactForm(ModelForm):

    def send_email(self):
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
    def send_email(self):
        admin_subject = "Newsletter Subcription Notification"
        admin_message = f"New User with E-mail address {self.cleaned_data['email']} susbcribed to our newsletter."
        recipient_list = ['ddctech.org@gmail.com']
        # admin
        send_mail(admin_subject,  admin_message,
                  DEFAULT_FROM_EMAIL, recipient_list)

    class Meta:
        model = NewsletterSubscription
        fields = ['email', ]
