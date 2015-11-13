from django.test import TestCase

from ..models import Slideshow
from ..serializers import SlideshowSerializer


class SlideshowSerializerTestCase(TestCase):

    """Tests for the `SlideshowSerializer`"""

    def test_instance_serialization(self):
        data = [{
            'slide1': 1,
            'slide2': 2
        }]
        slideshow = Slideshow.objects.create(slides=data, body='howdy')
        serializer = SlideshowSerializer(slideshow)
        expected_data = {
            'id': slideshow.id,
            'body': 'howdy',
            'slides': data
        }
        self.assertEqual(serializer.data, expected_data)

    def test_list_serialization(self):
        slideshow1_data = [{
            'slide1': 1,
            'slide2': 2
        }]
        slideshow1 = Slideshow.objects.create(slides=slideshow1_data, body='God')
        slideshow2_data = [{
            'slide1': 3,
            'slide2': 4
        }]
        slideshow2 = Slideshow.objects.create(slides=slideshow2_data, body='howdy')
        serializer = SlideshowSerializer(Slideshow.objects.all(), many=True)
        expected_data = [{
            'id': slideshow1.id,
            'body': 'God',
            'slides': slideshow1_data
        }, {
            'id': slideshow2.id,
            'body': 'howdy',
            'slides': slideshow2_data
        }]
        self.assertEqual(serializer.data, expected_data)

    def test_create(self):
        data = {
            'body': '',
            'slides': [{
                'slide1': 1,
                'slide2': 2
            }]
        }
        serializer = SlideshowSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Slideshow.objects.first(), serializer.instance)
