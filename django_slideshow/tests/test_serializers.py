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
        slideshow = Slideshow.objects.create(slides=data)
        serializer = SlideshowSerializer(slideshow)
        expected_data = {
            'id': slideshow.id,
            'slides': data,
            'detail_image': None,
            'detail_image_caption': None,
            'detail_image_alt': None
        }
        self.assertEqual(serializer.data, expected_data)

    def test_list_serialization(self):
        slideshow1_data = [{
            'slide1': 1,
            'slide2': 2
        }]
        slideshow1 = Slideshow.objects.create(slides=slideshow1_data)
        slideshow2_data = [{
            'slide1': 3,
            'slide2': 4
        }]
        slideshow2 = Slideshow.objects.create(slides=slideshow2_data)
        serializer = SlideshowSerializer(Slideshow.objects.all(), many=True)
        expected_data = [{
            'id': slideshow1.id,
            'slides': slideshow1_data,
            'detail_image': None,
            'detail_image_caption': None,
            'detail_image_alt': None
        }, {
            'id': slideshow2.id,
            'slides': slideshow2_data,
            'detail_image': None,
            'detail_image_caption': None,
            'detail_image_alt': None
        }]
        self.assertEqual(serializer.data, expected_data)

    def test_create(self):
        data = {
            'slides': [{
                'slide1': 1,
                'slide2': 2
            }],
            'detail_image': None,
            'detail_image_caption': None,
            'detail_image_alt': None
        }
        serializer = SlideshowSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Slideshow.objects.first(), serializer.instance)
