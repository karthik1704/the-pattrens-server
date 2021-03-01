from django.contrib import admin
from django.contrib.admin.options import TabularInline

from .models import (
    Category,
    Element,
    Platform,
    Pattern,
    Tag,
    UiApps,
    UiImages,
    Version,
)
# Register your models here.

class UiImagesAdmin(admin.StackedInline):
    model = UiImages
    extra = 2

class UiAPPSAdmin(admin.ModelAdmin):
    
    inlines = (UiImagesAdmin,)   
    list_display = ('name', 'created_at', 'modified_at')
    fieldsets = (
        (None, {'fields': ('name', 'url', 'copyright', 'image',)}),
        ('Category', {'fields': ('category', 'tag')}),
    )
    readonly_fields = ['created_at', 'modified_at']

admin.site.register(UiApps, UiAPPSAdmin)
admin.site.register(Category)
admin.site.register(Element)
admin.site.register(Platform)
admin.site.register(Pattern)
admin.site.register(Tag)
admin.site.register(Version)
admin.site.register(UiImages)