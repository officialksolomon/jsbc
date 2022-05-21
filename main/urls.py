from django.urls import path, include
from main.views import ContactView, NewsletterView
from django.views.generic import TemplateView

app_name = 'main'
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', TemplateView.as_view(template_name="main/about.html"), name='about'),
    path('portfolio/', TemplateView.as_view(template_name="main/portfolio.html"), name='portfolio'),
    path('newsletter/', NewsletterView.as_view(),
         name='newsletter'),
]
