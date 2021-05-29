from django.db import models
from django.conf import settings

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
