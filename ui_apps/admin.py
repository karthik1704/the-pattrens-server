from django.contrib import admin

from .models import UiApps
# Register your models here.
class UiAPPSAdmin(admin.ModelAdmin):
    
    class Meta:
        model = UiApps
        
    list_display = ('name', 'created_at', 'modified_at')
    fieldsets = (
        (None, {'fields': ('name', 'image',)}),
    )
    readonly_fields = ['created_at', 'modified_at']

admin.site.register(UiApps, UiAPPSAdmin)