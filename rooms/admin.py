from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero.")
def reset_price(model_admin, request, rooms):
    # print(model_admin)
    # print(dir(request))
    for room in rooms.all():
        # print(room.price)
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_price,)

    list_display = (
        "name",
        "owner",
        "price",
        "total_amenities",
        "rating",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )
    search_fields = (
        "name",
        "^price",
        "=owner__username",
    )

    search_help_text = "name, ^price, =owner__username"


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
