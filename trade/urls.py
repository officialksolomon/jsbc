
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from trade.views import TradeIndexView, SubscriptionView


app_name = 'trade'
urlpatterns = [
    path('index/', TradeIndexView.as_view(), name='index'),
    path('subscription/', SubscriptionView.as_view(), name='subscription'),

]
