from django.urls import path, include

from sm_system.common.views import index, CreateServiceInfo,\
    AllTasksListView, TaskEditView, TaskDeleteView, PriceListView

urlpatterns = [
    path('', index, name='home_page'),
    path('info/', include([
        path('create-task/', CreateServiceInfo.as_view(), name='create_task'),
        path('all-tasks/', AllTasksListView.as_view(), name='all_tasks'),
        path('edit-task/<int:pk>', TaskEditView.as_view(), name='edit_task'),
        path('delete-task/<int:pk>',TaskDeleteView.as_view(), name='delete_task'),
        path('price-list/<str:device_type>/', PriceListView.as_view(), name='price-list'),
    ])),
]
