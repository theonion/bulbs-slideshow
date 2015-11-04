from django.views.decorators.cache import cache_control
from django.views.generic.detail import DetailView

from .models import Slideshow


class SlideshowDetailView(DetailView):

    model = Slideshow


slideshow_detail = cache_control(max_age=600)(SlideshowDetailView.as_view())
