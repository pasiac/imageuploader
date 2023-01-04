import uuid
from django.db import models
from PIL import Image


def sanitize_filename(instance: models.Model, filename: str):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


def is_image_size_valid(img_size: tuple[int, int], req_size: tuple[int, int]):
    return True if img_size == req_size else False
    

def resize_image(image_path: str, req_size: tuple[int, int] = (256, 256)):
    img = Image.open(image_path)
    if is_image_size_valid(img.size, req_size):
        return
    img.thumbnail(req_size)
    img.save(image_path)


class UploadedImage(models.Model):
    image = models.ImageField("Uploaded image", upload_to=sanitize_filename)
    name = models.CharField(max_length=32)
    width = models.IntegerField()
    heigth = models.IntegerField()
    
    
    def save(self, *args, **kwargs) -> None:
        # heh
        super().save(*args, **kwargs)
        resize_image(self.image.path, (self.heigth, self.width))
