from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'created', 'last_login')
    list_filter = ('is_superuser', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),'fields': ('email', 'password1','password2' )}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)