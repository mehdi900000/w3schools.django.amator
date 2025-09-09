from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse



class Post(models.Model):
    subject = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.subject

    def get_absolute_url (self):
        return reverse("detail", kwargs={"pk": self.pk})