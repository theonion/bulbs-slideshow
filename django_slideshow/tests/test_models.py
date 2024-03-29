from django.test import TestCase

from ..models import Slideshow
from ..serializers import SlideshowSerializer


class SlideshowTestCase(TestCase):

    """Tests for the `Slideshow` model class."""

    def test_create(self):
        data = [{
            'slide1': 1,
            'slide2': 2
        }]
        slideshow = Slideshow.objects.create(slides=data)
        self.assertTrue(Slideshow.objects.filter(id=slideshow.id).exists())

    def test_get(self):
        data = [{
            'slide1': 1,
            'slide2': 2
        }]
        slideshow = Slideshow.objects.create(slides=data)
        id = slideshow.id

        slideshow = Slideshow.objects.get(id=id)
        self.assertIsInstance(slideshow, Slideshow)
        self.assertEqual(slideshow.id, id)
        self.assertEqual(slideshow.slides, data)

    def test_delete(self):
        data = [{
            'slide1': 1,
            'slide2': 2
        }]
        slideshow = Slideshow.objects.create(slides=data)
        slideshow.delete()
        self.assertFalse(Slideshow.objects.filter(id=slideshow.id))

    def test_get_serializer_class(self):
        serializer_class = Slideshow.get_serializer_class()
        self.assertEqual(serializer_class, SlideshowSerializer)
