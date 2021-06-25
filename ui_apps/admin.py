from django.contrib import admin
from django.contrib.admin.options import StackedInline, TabularInline

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

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ElementAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PaltformAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class VersionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('version_number',)}

class PatternAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class UiImagesAdmin(TabularInline):
    model = UiImages
    extra = 2

class VersionInline(StackedInline):
    model = Version
    extra = 2

class UiAPPSAdmin(admin.ModelAdmin):
    
    inlines = (VersionInline, UiImagesAdmin)   
    list_display = ('name', 'created_at', 'modified_at')
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'url', 'copyright', 'image',)}),
        ('Category', {'fields': ( 'platform','category', 'tag')}),
    )
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'modified_at']

    class Media:
        js=('ui_apps/app.js',)

admin.site.register(UiApps, UiAPPSAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Platform, PaltformAdmin)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(UiImages)