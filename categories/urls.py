from django.urls import path
from . import views, models

urlpatterns = [
    path(
        "",
        views.CategoryViewset.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",
        views.CategoryViewset.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "rooms/",
        views.CategoryRoomViewset.as_view(
            {
                "get": "list",
            }
        ),
    ),
]
