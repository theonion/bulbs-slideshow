from django.conf import settings
from rest_framework import serializers

from .models import Slideshow


BaseSerializer = getattr(settings, 'DEFAULT_SERIALIZER', serializers.ModelSerializer)


class SlideshowSerializer(BaseSerializer):

    class Meta:
        model = Slideshow
