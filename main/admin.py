from django.contrib import admin
from main.models import Contact, NewsletterSubscription

# Register your models here.
admin.site.register(Contact)
admin.site.register(NewsletterSubscription)
