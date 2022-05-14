from django.urls import path, include
from main.views import ContactView
from django.views.generic import TemplateView

app_name = 'main'
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', TemplateView.as_view(template_name="main/about.html"), name='about'),
]
