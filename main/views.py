from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.db import IntegrityError
from main.html_response import contact_success, contact_failure, newsletter_success, newsletter_failure

from main.forms import ContactForm, NewsletterForm

# Create your views here.


class HomepageView(View):
    #
    def get(self, request):
        return render(request, 'main/index.html')


# Contact page view.
class ContactView(View):
    #
    def get(self, request):
        return render(request, 'main/contact.html')
    #

    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse(contact_success)
        else:
            return HttpResponse(contact_failure)


class NewsletterView(View):
    def post(self, request):
        form = NewsletterForm(request.POST or None)

        if form.is_valid():
            form.save()
            return HttpResponse(newsletter_success)
        else:
            return HttpResponse(newsletter_failure)
