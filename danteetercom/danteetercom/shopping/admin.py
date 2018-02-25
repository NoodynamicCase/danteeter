from django.contrib import admin
from .models import Shopping
from import_export.admin import ImportExportModelAdmin

class ShoppingAdmin(ImportExportModelAdmin):
    # list_display = ('name', 'email', 'phone', 'follow_up', 'timestamp_added',)
    # search_fields = ('name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    # ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = Shopping

admin.site.register(Shopping, ImportExportModelAdmin)
