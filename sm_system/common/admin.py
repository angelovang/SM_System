from django.contrib import admin

from sm_system.common.models import ServiceInfo


@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    pass
