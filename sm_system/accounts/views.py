from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, logout


from sm_system.accounts.forms import RegisterEmplForm
from sm_system.accounts.models import SmsUser

UserModel = get_user_model()


class RegisterEmplView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterEmplForm
    success_url = reverse_lazy('login_user')


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    next_page = 'home_page'

def logout_user(request):
    logout(request)
    return redirect('home_page')

# class LogoutUserView(auth_views.LogoutView):
#     #template_name = 'accounts/logout_page.html'
#     next_page = 'home_page'


class EmployeesListView(views.ListView):
    model = SmsUser
    template_name = 'accounts/employees_list.html'
    def get_queryset(self):
        return super().get_queryset()


class EmployeesDetailsView(views.DetailView):
    template_name = 'accounts/employees_details.html'
    model = UserModel

    profile_image = static('static/images/user_2.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_image'] = self.profile_image
        return context


# class ProfileEditView(views.UpdateView):
#     template_name = 'accounts/profile-edit-page.html'
#
#
# class ProfileDeleteView(views.DeleteView):
#     template_name = 'accounts/profile-delete-page.html'
