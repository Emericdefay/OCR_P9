from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserFollows(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_by")

    class Meta:
        """[summary]
        """
        unique_together = ('user', 'followed_user',)