from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    class Meta:
        ordering = ['-name']
    def __str__(self):
        return self.name[0:50]