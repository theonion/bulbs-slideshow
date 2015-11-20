from django.core.urlresolvers import reverse
from django.db import models

from djbetty import ImageField
from jsonfield import JSONField
from parent_swap import swap

from .field import ElasticsearchImageField


class Slideshow(swap.get_base_model()):

    slides = JSONField(default=[], blank=True)
    # body = models.TextField(blank=True, default="")
    detail_image_caption = models.CharField(max_length=255, null=True, blank=True, editable=False)
    detail_image_alt = models.CharField(max_length=255, null=True, blank=True, editable=False)
    detail_image = ImageField(
        null=True,
        default=None,
        blank=True,
        alt_field="detail_image_alt",
        caption_field="detail_image_caption"
    )

    def get_absolute_url(self):
        return reverse("slideshows:slideshow-detail", kwargs={"slug": self.slug, "pk": self.pk})

    def get_template(self):
        return "partials/slideshow-detail.html"

    @classmethod
    def get_serializer_class(cls):
        # Do not like this, but we currently rely on the `get_serializer_class` method.
        from .serializers import SlideshowSerializer
        return SlideshowSerializer

    class Meta:
        abstract = False

    class Mapping(swap.BaseMapping):
        detail_image = ElasticsearchImageField()

        class Meta:
            excludes = ("slides",)
