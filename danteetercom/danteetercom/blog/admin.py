from django.contrib import admin
from .models import Blog
from import_export.admin import ImportExportModelAdmin

class BlogAdmin(ImportExportModelAdmin):
    list_display = ('timestamp_added', 'post_title', 'post_category', 'public_private',)
    # search_fields = ('name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    # ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = Blog

admin.site.register(Blog, ImportExportModelAdmin)
