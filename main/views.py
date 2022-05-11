from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

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
        pass
