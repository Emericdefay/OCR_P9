from django.db import models

# Create your models here.

class Review(models.Model):
    ticket = models.ForeignKey(to="create_review.Ticket", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(max_length=1024, validators={MinValueValidator(0), MaxValueValidator(5)})
    user = models.ForeignKey(to="settings.AUTH_USER_MODEL", on_delete=models.CASCADE)
    headline =models.CharField(max_length=128)
    body =models.TextField(max_length=8192, blank=True)
    time_creted = models.DateTimeField(auto_now_add=True)