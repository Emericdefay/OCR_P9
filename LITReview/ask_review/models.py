from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """[summary]

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField()

    def __str__(self):
        return self.title
