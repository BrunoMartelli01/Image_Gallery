from django.db import models
from django.utils import timezone


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('users.MyUser', on_delete=models.PROTECT)
