from django.contrib import admin
from .models import returnItemModel

# Register your models here.


@admin.register(returnItemModel)
class returnItemAdmin(admin.ModelAdmin):
    list_display = (
        "item_type",
        "item_description",
        "location_found",
        "date_found",
        "approval",
    )
    list_filter = ["approval"]
    actions = ['approve_items', 'disapprove_items']

    def approve_items(self, request, queryset):
        queryset.update(approval=True)
    approve_items.short_description = "Approve selected items"

    def disapprove_items(self, request, queryset):
        queryset.update(approval=False)
    disapprove_items.short_description = "Disapprove selected items"
