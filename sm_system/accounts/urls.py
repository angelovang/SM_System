from django.urls import path

from sm_system.accounts.views import RegisterEmplView, LoginUserView, EmployeesDetailsView, logout_user, \
    EmployeesListView

urlpatterns = [
    path('register/', RegisterEmplView.as_view(), name='register_employee'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('employees_list/', EmployeesListView.as_view(), name='employees_list'),
    # path('edit_employee/<int:pk>', EmployeeEditView.as_view(), name='edit_employee'),
    # path('delete_employee/<int:pk>', EmployeeDeleteView.as_view(), name='delete_employee'),
]