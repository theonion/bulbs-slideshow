from djbetty.serializers import ImageFieldSerializer
from parent_swap import swap

from .models import Slideshow


class SlideshowSerializer(swap.get_base_serializer()):

    detail_image = ImageFieldSerializer(required=False, allow_null=True)

    class Meta:
        model = Slideshow
