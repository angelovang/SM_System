from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('api/', include('sm_system.api.urls', namespace='api')),
    path('',include('sm_system.common.urls')),
    path('accounts/', include('sm_system.accounts.urls')),
    path('clients/', include('sm_system.clients.urls')),
    path('reception/', include('sm_system.reception.urls')),
    path('management/', include('sm_system.management.urls')),
]

