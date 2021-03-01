from django.contrib import admin

from .models import UserRequest
# Register your models here.

class UserRequestAdmin(admin.ModelAdmin):

    list_display  = ('id', 'app_name')


admin.site.register(UserRequest, UserRequestAdmin)