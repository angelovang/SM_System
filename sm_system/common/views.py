from django.contrib.auth import mixins as auth_mixins

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as generic_views
from django.views.generic import ListView, UpdateView, DeleteView

from sm_system.common.models import ServiceInfo


def index(request):
    return render(request, 'common/service_wellcome.html')


class CreateServiceInfo(auth_mixins.LoginRequiredMixin, generic_views.CreateView):
    model = ServiceInfo
    fields = '__all__'
    labels = {
        'device': 'Device type:',
        'description': 'Repair description:',
        'price': 'Price as text:'
    }
    template_name = 'common/create-service-task.html'
    success_url = '/info/create_task'


class AllTasksListView(auth_mixins.LoginRequiredMixin, ListView):
    model = ServiceInfo
    template_name = 'common/all-tasks.html'
    paginate_by = 7
    def get_queryset(self):
        return super().get_queryset()


class TaskEditView(auth_mixins.LoginRequiredMixin, UpdateView):
    model = ServiceInfo
    fields = '__all__'
    template_name = 'common/edit-task.html'
    success_url = '/info/all_tasks'


class TaskDeleteView(auth_mixins.LoginRequiredMixin, DeleteView):
    template_name = 'common/delete-task.html'
    model = ServiceInfo
    success_url = reverse_lazy('all_tasks')


class PriceListView(ListView):
    model = ServiceInfo
    template_name = 'common/price-list.html'
    context_object_name = 'device_list'
    device_mapping = {
        'computer': 'Computers',
        'laptop': 'Laptops',
        'monitor': 'Monitors',
        'printer': 'Printers',
    }

    def get_queryset(self):
        device_type = self.kwargs.get('device_type')
        if device_type in self.device_mapping:
            return super().get_queryset().filter(device=device_type)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['device_category'] = self.device_mapping.get(self.kwargs.get('device_type'))
        return context
