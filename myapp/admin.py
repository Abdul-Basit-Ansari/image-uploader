from django.contrib import admin

# Register your models here.
from .models import Image
# Register your models here.

admin.site.register(Image)
# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#  list_display = ['id', 'photo', 'date']