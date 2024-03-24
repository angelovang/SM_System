from django.urls import path
from sm_system.reception.views import OrderCreateView, OrdersListView, OrderEditView, OrderDeleteView, OrderDetailsView

urlpatterns = [
    path('create_order/', OrderCreateView.as_view(), name='create_order'),
    path('orders_list/', OrdersListView.as_view(), name='orders_list'),
    path('edit_order/<int:pk>', OrderEditView.as_view(), name='edit_order'),
    path('delete_order/<int:pk>', OrderDeleteView.as_view(), name='delete_order'),
    path('order_details/<int:pk>', OrderDetailsView.as_view(), name='order_details'),
]