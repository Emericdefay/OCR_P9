from django.db import models
from django.contrib.auth.models import User


class UserFollows(models.Model):
    """Model user/follow for BDD.

    Args:
        models ([module]): Model SQL manipulation
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followed_by")

    class Meta:
        """ Return a tuple whose items are the same
        and in the same order as iterable's items.
        """
        unique_together = ('user', 'followed_user',)
