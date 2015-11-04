from rest_framework import viewsets

from .models import Slideshow
from .serializers import SlideshowSerializer


class SlideshowViewSet(viewsets.ModelViewSet):
    model = Slideshow
    queryset = Slideshow.objects.all()
    serializer_class = SlideshowSerializer
