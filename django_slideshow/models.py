from django.apps import apps
from django.conf import settings
from django.db import models

from jsonfield import JSONField


def get_base_class():
    default_class_name = getattr(settings, 'DEFAULT_BASE_CLASS', None)

    if default_class_name:
        try:
            sp = default_class_name.split('.')
            app_name, cls_name = sp[-2], sp[-1]
            app = apps.get_app(app_name)
            base_cls = getattr(app, cls_name, None)
            if base_cls:
                return base_cls
        except:
            pass

    return models.Model


class AbstractSlideshow(get_base_class()):
    """
    Added to avoid the current conflict of primary_key fields. models.E005.
    """

    class Meta:
        abstract = True

    @classmethod
    def get_serializer_class(cls):
        # Do not like this, but we currently rely on the `get_serializer_class` method.
        from .serializers import SlideshowSerializer
        return SlideshowSerializer


class Slideshow(AbstractSlideshow):

    slides = JSONField(default=[], blank=True)

    class Meta:
        abstract = False
