from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """
    Needed for better UI representation on admin panel
    """
    list_display = [
        'name',
        'address',
        'delivery',
        'phone_number',
    ]

    list_filter = [
        'delivery',
    ]
