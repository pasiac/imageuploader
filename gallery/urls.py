from django.urls import include, path
from rest_framework import routers

from gallery.views import UploadedImagesViewSet

router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')


urlpatterns = [
    path('', include(router.urls)),
]