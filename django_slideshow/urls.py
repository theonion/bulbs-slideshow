from django.conf import settings
from django.conf.urls import patterns, include, url

from .routers import router


api_route = getattr(settings, 'API_ROUTE', r'api/')

slideshow_patterns = patterns(
    "",
    url(api_route, include(router.urls)),
)
