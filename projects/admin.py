from django.contrib import admin

from projects.models import Platform, Project, Category, Element, Pattern,ProjectImage,ProjectVersion
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk','project_name', 'url','copy_right','category','created_at', 'modified_at')
    fieldsets = (
        (None, {'fields': ('project_name',  'url', 'copy_right', 'image',)}),
        ('Category', {'fields': ( 'platform','category', )}),
    )
    readonly_fields = ['created_at', 'modified_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','category_name', 'created_at', 'modified_at')

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('pk','platform_name', 'created_at', 'modified_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Pattern)
admin.site.register(Element)
admin.site.register(ProjectVersion)
admin.site.register(ProjectImage)