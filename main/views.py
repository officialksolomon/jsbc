from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.db import IntegrityError
from main.html_response import contact_success, contact_failure, newsletter_success, newsletter_failure
from main.forms import ContactForm, NewsletterForm
from main.email import Email
import threading


# Create your views here.

def new_user_notification(request):
    """Notify admins when a new user visit the hompage"""
    # if 'is_new_user' not in request.session:
    #     email_thread = threading.Thread(target=Email.new_visit_email)
    #     email_thread.start()
    # request.session['is_new_user'] == False
    pass


class HomepageView(View):
    def get(self, request):
        new_user_notification(request)
        return render(request, 'main/index.html')


# Contact page view.
class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html')

    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            context = {'status': 'success',
                       'message': f"Dear {form.cleaned_data['name']}, we have successfully received your message."}
            # speedup I/O bounding email sending with threading
            email_thread = threading.Thread(target=form.send_email)
            email_thread.start()
            return render(request, 'main/partials/contact_response.html', context)
        else:
            context = {'status': 'danger',
                       'message': 'Sorry we didnt receive your message please try again'}
            return render(request, 'main/partials/contact_response.html', context)



class NewsletterView(View):
    def get(self, email):
        pass
    def post(self, request):
        form = NewsletterForm(request.POST or None)
        if form.is_valid():
            form.save()
            context = {'status': 'success',
                       'message': f"{form.cleaned_data['email']},have been successfully suscribed"}
            email_thread = threading.Thread(target=form.send_email)
            email_thread.start()
            # form.send_email()
            return render(request, 'main/partials/newsletter_response.html', context)
        else:
            context = {'status': 'danger',
                       'message': f"Failed to suscribe, please try again or try with a different E-mail."}
            return render(request, 'main/partials/newsletter_response.html', context)


