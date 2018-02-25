from django.contrib import admin
from .models import Contacts
from import_export.admin import ImportExportModelAdmin

class ContactsAdmin(ImportExportModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone', 'follow_up', 'timestamp_added',)
    search_fields = ('last_name', 'first_name', 'timestamp',)
    # date_hierarchy = 'timestamp'
    ordering = ('timestamp_added',)
    # list_filter = ('category','timestamp',)
    # date_hierarchy = 'timestamp'
    # filter_horizontal = ('category',) -- use for ManytoMany fields
    class Meta:
        model = Contacts

admin.site.register(Contacts, ImportExportModelAdmin)
