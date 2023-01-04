from rest_framework import viewsets, filters
from gallery.serializers import UploadedImageSerializer
from gallery.models import UploadedImage


class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name',]
