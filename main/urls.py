from django.urls import path, include
from main.views import ContactView

app_name = 'main'
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]
