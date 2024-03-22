from django.urls import path, include

from sm_system.clients.views import ClientCreateView, clients_view, ClientListView, ClientEditView, ClientDeleteView

urlpatterns = (
    path('', clients_view, name='client_view'),
    path('create_client/',ClientCreateView.as_view(), name='create_client'),
    path('client_list/', ClientListView.as_view(), name='clients_list'),
    path('edit_client/<int:pk>', ClientEditView.as_view(), name='edit_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client')
    )
