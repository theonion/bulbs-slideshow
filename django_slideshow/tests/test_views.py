import json
import sys

from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Slideshow


class SlideshowAPITestCase(TestCase):

    def test_router_registered(self):
        list_url = reverse('slideshow-list')
        self.assertEqual(list_url, '/api/slideshows/')
        detail_url = reverse('slideshow-detail', kwargs={'pk': 1})
        self.assertEqual(detail_url, '/api/slideshows/1/')

    def test_post(self):
        list_url = reverse('slideshow-list')
        slide_data = [{
            'slide1': 1,
            'slide2': 2
        }]
        data = {
            'slides': slide_data
        }
        resp = self.client.post(list_url, json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        id = resp.data.get('id')
        slides = resp.data.get('slides')
        self.assertIsNotNone(id)
        if sys.version_info.major < 3:
            self.assertItemsEqual(slides, slide_data)
        else:
            self.assertCountEqual(slides, slide_data)
        slideshow = Slideshow.objects.get(id=int(id))
        self.assertIsNotNone(slideshow)
        if sys.version_info.major < 3:
            self.assertItemsEqual(slideshow.slides, slide_data)
        else:
            self.assertCountEqual(slideshow.slides, slide_data)

    def test_get(self):
        slide_data = [{
            'slide1': 1,
            'slide2': 2
        }]
        slideshow = Slideshow.objects.create(slides=slide_data)
        detail_url = reverse('slideshow-detail', kwargs={'pk': slideshow.id})
        resp = self.client.get(detail_url)
        self.assertEqual(resp.status_code, 200)

        expected_slideshow = {
            'id': slideshow.id,
            'slides': slide_data
        }
        if sys.version_info.major < 3:
            self.assertItemsEqual(resp.data, expected_slideshow)
        else:
            self.assertCountEqual(resp.data, expected_slideshow)

    def test_put(self):
        slide_data = [{
            'slide1': 1,
            'slide2': 2
        }]
        slideshow = Slideshow.objects.create(slides=slide_data)
        detail_url = reverse('slideshow-detail', kwargs={'pk': slideshow.id})
        resp = self.client.get(detail_url)
        data = resp.data
        slide_data[0].update({'slide3': 3})
        data['slides'] = slide_data
        resp = self.client.put(detail_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        slides = resp.data.get('slides')
        self.assertIn(('slide3', 3), slides[0].items())
