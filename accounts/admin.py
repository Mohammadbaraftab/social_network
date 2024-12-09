from django.contrib import admin
from .models import Profile, Country


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number", "is_active", "created_time")
    list_filter = ("is_active", "created_time")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_time")