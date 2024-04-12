from django.urls import path

from sm_system.api.views import APIClientListView

app_name = "api"

urlpatterns = [
    path('clients/', APIClientListView.as_view(), name='clients_list'),
]