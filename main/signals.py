from django.core.signals import request_started
from django.dispatch import receiver
from main.email import Email
import threading

# @receiver(request_started)
# def new_visit(sender, environ, **kwargs):
#     if environ['REQUEST_METHOD'] == "GET" and environ['PATH_INFO'] == "/":
#         print(environ['HTTP_COOKIE'], 'hERE')
#         email_thread = threading.Thread(target=Email.visit_email)
#         # email_thread.start()

