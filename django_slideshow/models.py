from django.db import models

from jsonfield import JSONField


class Slideshow(models.Model):

    slides = JSONField(default=[], blank=True)

    @classmethod
    def get_serializer_class(cls):
        # Do not like this, but we currently rely on the `get_serializer_class` method.
        from .serializers import SlideshowSerializer
        return SlideshowSerializer
