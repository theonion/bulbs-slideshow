from django.conf import settings

from rest_framework import serializers

from djbetty.serializers import ImageFieldSerializer

from .models import Slideshow


def get_base_serializer():
    default_serializer_name = getattr(settings, 'DEFAULT_SERIALIZER', None)
    if default_serializer_name:
        try:
            mod_name, sp, serializer = default_serializer_name.rpartition('.')
            mod = __import__(mod_name, fromlist=[''])
            serializer = getattr(mod, serializer, None)
            if serializer:
                return serializer
        except:
            pass
    return serializers.ModelSerializer


BaseSerializer = get_base_serializer()


class SlideshowSerializer(BaseSerializer):

    detail_image = ImageFieldSerializer(required=False, allow_null=True)

    class Meta:
        model = Slideshow
