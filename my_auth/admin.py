from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "username", "is_staff", "is_active")

    email_field = ((None, {"fields": ("email",)}),)
    fieldsets = list(UserAdmin.fieldsets)

    if all(
        "email" not in field_info["fields"]
        for _, field_info in fieldsets
        if "fields" in field_info
    ):
        fieldsets.append(email_field)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "bio"]
    list_editable = ["bio", "name"]


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
