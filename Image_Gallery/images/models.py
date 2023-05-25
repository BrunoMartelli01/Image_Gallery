from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)

