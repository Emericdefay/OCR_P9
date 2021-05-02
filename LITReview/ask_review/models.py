from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """Ticket model for BDD

    Args:
        models ([module]): models SQL manipulation
    """
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
