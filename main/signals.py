from django.core.signals import request_started
from django.dispatch import receiver


@receiver(request_started)
def new_visit(sender, environ, **kwargs):
    print(environ['REQUEST_METHOD'])
