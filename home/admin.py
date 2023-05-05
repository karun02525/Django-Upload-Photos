from django.contrib import admin
from .models import ImageModel

# Register your models here.
@admin.register(ImageModel)
class ImageAdminModel(admin.ModelAdmin):
    list_display = ['id','image','date']
