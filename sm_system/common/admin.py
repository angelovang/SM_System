from django.contrib import admin

from sm_system.common.models import ServiceInfo


@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'device', 'description', 'price']
    search_fields = ['device']
    search_help_text = 'Search by device'