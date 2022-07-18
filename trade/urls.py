
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from trade.views import TradeIndex


app_name = 'trade'
urlpatterns = [
    path('index/', TradeIndex.as_view(), name='index'),

]
