from django.contrib import admin
from .models import Project, ProjectCategory


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'name',
        'descriptive_name',
        'description',
        'date',
        'location',
        'image',
    )

    ordering = ('sku',)


class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
