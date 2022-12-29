from django.contrib import admin
from .models import Photo, Video


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "file",
        "room",
        "experience",
        "created_at",
    )


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
