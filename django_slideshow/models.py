from django.db import models

from jsonfield import JSONField


class Slideshow(models.Model):
    slides = JSONField(default=[], blank=True)
