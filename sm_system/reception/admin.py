from django.contrib import admin

from sm_system.reception.models import ServiceOrder


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'so_id','accept_date', 'close_date',
                    'client', 'technician',
                    'device_type', 'device_data',
                    'issue_description', 'status']
    list_filter = ['accept_date', 'status', 'technician']
    fields = [('accept_date', 'close_date'),
                    ('client', 'technician'),
                    ('device_type', 'device_data'),
                    'issue_description', 'status']








