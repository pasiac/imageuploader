from rest_framework import serializers
from gallery.models import UploadedImage


class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('pk', 'image', 'name', 'width', 'heigth',)
