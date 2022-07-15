from pkgutil import ImpImporter
from django.urls import path, include
from main.views import ContactView, NewsletterView
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from . sitemaps import StaticSitemap


sitemaps = {
    'blog': StaticSitemap
}

app_name = 'main'
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', TemplateView.as_view(template_name="main/about.html"), name='about'),
    path('portfolio/', TemplateView.as_view(template_name="main/portfolio.html"), name='portfolio'),
    path('terms/', TemplateView.as_view(template_name="main/terms.html"), name='terms'),
    path('newsletter/', NewsletterView.as_view(),
         name='newsletter'),
    #
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
