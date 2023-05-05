from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image=models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now_add=True)
