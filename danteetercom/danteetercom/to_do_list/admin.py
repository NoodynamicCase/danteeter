from django.contrib import admin
from .models import To_Do_List, To_Do_List_File, DailyLog
from import_export.admin import ImportExportModelAdmin

class To_Do_ListAdmin(ImportExportModelAdmin):
    # list_display = ('name', 'email', 'phone', 'follow_up', 'timestamp_added',)
    # search_fields = ('name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    # ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = To_Do_List

admin.site.register(To_Do_List, ImportExportModelAdmin)

class To_Do_List_FileAdmin(ImportExportModelAdmin):
    # list_display = ('name', 'email', 'phone', 'follow_up', 'timestamp_added',)
    # search_fields = ('name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    # ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = To_Do_List_File

admin.site.register(To_Do_List_File, ImportExportModelAdmin)

class DailyLogAdmin(ImportExportModelAdmin):
    # list_display = ('name', 'email', 'phone', 'follow_up', 'timestamp_added',)
    # search_fields = ('name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    # ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = DailyLog

admin.site.register(DailyLog, ImportExportModelAdmin)
