from rest_framework.routers import DefaultRouter

from .viewsets import SlideshowViewSet

router = DefaultRouter(trailing_slash=True)
router.register("slideshows", SlideshowViewSet, "slideshow")
