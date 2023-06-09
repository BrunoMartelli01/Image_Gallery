from datetime import datetime

from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from .models import Image


class ImagesSerializer(serializers.ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = Image
        fields = ['id', 'image', 'title', 'created', 'user']

