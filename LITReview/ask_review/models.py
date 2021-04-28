from django.db import models

# Create your models here.

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to="settings.AUTH_USER_MODEL", on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)