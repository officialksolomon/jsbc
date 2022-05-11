from django.urls import path, include
from main.views import ContactView
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]
