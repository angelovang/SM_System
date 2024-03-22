from django.contrib import admin

from sm_system.clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'phone_number']
    list_display_links = ['id', 'email']
    search_fields = ['email']
    search_help_text = 'Search by email'
