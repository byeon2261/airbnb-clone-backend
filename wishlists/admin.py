from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "created_at",
        "updated_at",
    )
