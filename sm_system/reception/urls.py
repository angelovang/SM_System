from django.urls import path
from sm_system.reception.views import \
    OrderCreateView, \
    OrdersListView, \
    OrderEditView, \
    OrderDeleteView, \
    EndRepairView, SelectOrderView, start_repair

urlpatterns = [
    path('create_order/', OrderCreateView.as_view(), name='create_order'),
    path('orders_list/', OrdersListView.as_view(), name='orders_list'),
    path('edit_order/<int:pk>', OrderEditView.as_view(), name='edit_order'),
    path('delete_order/<int:pk>', OrderDeleteView.as_view(), name='delete_order'),
    path('select_order/', SelectOrderView.as_view(), name='select_order'),
    path('start_repair/<int:pk>', start_repair, name='start_repair'),
    path('end_repair/', EndRepairView.as_view(), name='end_repair'),
]
