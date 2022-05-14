from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

from main.forms import ContactForm

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
        if request.user.is_authenticated:
            form = ContactForm(request.POST or None)
            if form.is_valid():
                form.save()
