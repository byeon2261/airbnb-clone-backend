from django.contrib import admin
from .models import Review


class RatingFilter(admin.SimpleListFilter):
    title = "Rating Filter"

    parameter_name = "rating_filter"

    def lookups(self, request, model_admin):
        return (
            ("up", "3⭐️ then Up"),
            ("down", "3⭐️ then Down"),
        )

    def queryset(self, request, queryset):
        rating_up_down = self.value()
        if rating_up_down == "up":
            return queryset.filter(rating__gt=3)
        elif rating_up_down == "down":
            return queryset.filter(rating__lte=3)
        else:
            return queryset


class WordFilter(admin.SimpleListFilter):
    title = "Word filter!"
    parameter_name = "word"

    # def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
        ]

    # def queryset(self, request: Any, queryset: QuerySet[Any]) -> Optional[QuerySet[Any]]:
    def queryset(self, request, queryset):
        word = self.value()
        if word:
            return queryset.filter(payload__contains=word)
        else:
            return queryset


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
        "room",
        "experience",
        "created_at",
    )
    list_filter = (
        RatingFilter,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
