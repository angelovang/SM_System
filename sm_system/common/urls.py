from django.urls import path, include

from sm_system.common.views import index, CreateServiceInfo, ComputersListView, LaptopsListView, MonitorsListView, \
    PrintersListView, AllTasksListView, TaskEditView , TaskDeleteView

urlpatterns = [
    path('', index, name='home_page'),
    path('info/', include([
        path('create-task/', CreateServiceInfo.as_view(), name='create_task'),
        path('computers/', ComputersListView.as_view(), name='computers'),
        path('laptops/', LaptopsListView.as_view(), name='laptops'),
        path('monitors/', MonitorsListView.as_view(), name='monitors'),
        path('printers/', PrintersListView.as_view(), name='printers'),
        path('all-tasks/', AllTasksListView.as_view(), name='all_tasks'),
        path('edit-task/<int:pk>', TaskEditView.as_view(), name='edit_task'),
        path('delete-task/<int:pk>',TaskDeleteView.as_view(), name='delete_task'),
    ])),
]
