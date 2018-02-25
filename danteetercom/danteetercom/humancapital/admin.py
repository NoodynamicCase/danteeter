from django.contrib import admin
from .models import HumanCapitalPost, HumanCapitalJargon, HumanCapitalSource
from import_export.admin import ImportExportModelAdmin

class HumanCapitalPostAdmin(ImportExportModelAdmin):
    # list_display = ('name', 'email', 'phone', 'follow_up', 'timestamp_added',)
    # search_fields = ('name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = HumanCapitalPost

admin.site.register(HumanCapitalPost, ImportExportModelAdmin)

class HumanCapitalJargonAdmin(ImportExportModelAdmin):
    # list_display = ('name', 'email', 'phone', 'follow_up', 'timestamp_added',)
    # search_fields = ('name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = HumanCapitalJargon

admin.site.register(HumanCapitalJargon, ImportExportModelAdmin)


class HumanCapitalSourceAdmin(ImportExportModelAdmin):
    # list_display = ('name', 'email', 'phone', 'follow_up', 'timestamp_added',)
    # search_fields = ('name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = HumanCapitalSource

admin.site.register(HumanCapitalSource, ImportExportModelAdmin)
