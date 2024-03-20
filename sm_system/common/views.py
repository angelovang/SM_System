from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.views.generic import ListView, UpdateView, DeleteView

from sm_system.common.models import ServiceInfo


def index(request):
    return render(request, 'common/service_wellcome.html')


class CreateServiceInfo(generic_views.CreateView):
    model = ServiceInfo
    fields = '__all__'
    labels = {
        'device': 'Device type:',
        'description': 'Repair description:',
        'price': 'Price as text:'
    }
    template_name = 'common/create_service_task.html'
    success_url = '/info/create_task'


class AllTasksListView(ListView):
    model = ServiceInfo
    template_name = 'common/all_tasks.html'

    def get_queryset(self):
        return super().get_queryset()


class TaskEditView(UpdateView):
    model = ServiceInfo
    fields = '__all__'
    template_name = 'common/edit_task.html'
    success_url = '/info/all_tasks'


class TaskDeleteView(DeleteView):
    template_name = 'common/delete_task.html'
    model = ServiceInfo
    success_url = reverse_lazy('all_tasks')


class ComputersListView(ListView):
    model = ServiceInfo
    template_name = 'common/computers.html'

    def get_queryset(self):
        return super().get_queryset().filter(device='computer')


class LaptopsListView(ListView):
    model = ServiceInfo
    template_name = 'common/laptops.html'

    def get_queryset(self):
        return super().get_queryset().filter(device='laptop')


class MonitorsListView(ListView):
    model = ServiceInfo
    template_name = 'common/monitors.html'

    def get_queryset(self):
        return super().get_queryset().filter(device='monitor')


class PrintersListView(ListView):
    model = ServiceInfo
    template_name = 'common/printers.html'

    def get_queryset(self):
        return super().get_queryset().filter(device='printer')



