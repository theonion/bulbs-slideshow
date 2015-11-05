from django.conf import settings
from django.views.decorators.cache import cache_control
from django.views.generic.detail import DetailView

from .models import Slideshow


def get_base_detail_view():
    default_detail_view = getattr(settings, 'DEFAULT_DETAIL_VIEW', None)
    if default_detail_view:
        try:
            mod_name, sp, view_name = default_detail_view.rpartition('.')
            mod = __import__(mod_name, fromlist=[''])
            view = getattr(mod, view_name, None)
            if view:
                return view
        except:
            pass
    return DetailView


BaseView = get_base_detail_view()


class SlideshowDetailView(BaseView):

    model = Slideshow


slideshow_detail = cache_control(max_age=600)(SlideshowDetailView.as_view())
