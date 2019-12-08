from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Message(models.Model):
    sender  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    message_read = models.BooleanField(default=False)
