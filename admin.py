from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group as OldGroup
from django.utils.translation import gettext_lazy as _

from .models import User, Group

# Register your models here.
admin.site.unregister(OldGroup)
admin.site.register(Group)

# Register user and custom admin panel
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ("email", "username", "date_joined", "is_staff")
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("-date_joined",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username", "first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
