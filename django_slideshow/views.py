from django.views.decorators.cache import cache_control

from parent_swap import swap

from .models import Slideshow


class SlideshowDetailView(swap.get_base_view()):

    model = Slideshow


slideshow_detail = cache_control(max_age=600)(SlideshowDetailView.as_view())
