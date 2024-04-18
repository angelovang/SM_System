from django.contrib import admin

from sm_system.accounts.models import SmsUser


@admin.register(SmsUser)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number']
    list_display_links = ['id', 'email']
    search_fields = ['username']
    search_help_text = 'Search by username'

