from django.contrib import admin
from main.models import Contact, NewsletterSubscription, Profile

# Register your models here.
admin.site.register(Contact)
admin.site.register(NewsletterSubscription)
admin.site.register(Profile)
