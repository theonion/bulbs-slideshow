from django.conf import settings
from django.conf.urls import patterns, include, url

from .routers import router


API_ROUTE = getattr(settings, 'API_ROUTE', r'api/')

slideshow_patterns = patterns(
    "",
    url(API_ROUTE, include(router.urls)),
)

urlpatterns = patterns(
    "django_slideshow.views",

    url(
        r'^slideshow/(?P<slug>[\w-]+)-(?P<pk>\d+)/?$', 'slideshow_detail', name='slideshow-detail'
    ),
)
