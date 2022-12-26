from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "kind",
        "created_at",
    )

    list_filter = ("kind",)


# def get_form(self, request, obj=None, **kwargs):
#     form = super(RoomAdmin, self).get_form(request, obj, **kwargs)
#     form.base_fields['category'].queryset = Category.objects.filter(kind='rooms')
#     return form
