from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role
from django.contrib.auth.models import Permission

@admin.register(User)
class CUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )


class RoleAdmin(admin.ModelAdmin):
    pass


class PermissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Role, RoleAdmin)
admin.site.register(Permission, PermissionAdmin)