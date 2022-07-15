from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home',  'main:about', 'main:portfolio', 'main:terms']

    def location(self, item):
        return reverse(item)
