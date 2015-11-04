from rest_framework.routers import DefaultRouter

from .views import SlideshowViewSet

router = DefaultRouter(trailing_slash=True)
router.register("slideshows", SlideshowViewSet, "slideshow")
