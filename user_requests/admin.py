from django.contrib import admin

from .models import UserRequest
# Register your models here.

def mark_is_done(self, request, queryset):
    for obj in queryset:
        if not obj.is_done:
            obj.is_done = True
            obj.save()

class UserRequestAdmin(admin.ModelAdmin):

    list_display  = ('app_name', 'id', 'app_url', 'platform', 'name', 'email', 'promotion', 'is_done')
    list_filter = ('is_done', 'created_at', 'promotion')
    actions = [mark_is_done]

   

admin.site.register(UserRequest, UserRequestAdmin)