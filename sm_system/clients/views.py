from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from sm_system.clients.models import Client
from sm_system.reception.models import ServiceOrder, OrdersHistory


def clients_view(request):
    return render(request, 'clients/client_view.html')


def client_order_info(request):
    search_code = request.GET.get('search2')

    current_order = ServiceOrder.objects.filter(so_id=search_code).get()
    current_history = OrdersHistory.objects.filter(order_id=current_order.pk).get()

    context = {
        'current_order': current_order,
        'current_history': current_history,
    }
    return render(request, 'clients/client_order_info.html', context)


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/create_client.html'
    success_url = reverse_lazy('clients_list')


class ClientListView(ListView):
    model = Client
    template_name = 'clients/clients_list.html'

    def get_queryset(self):
        return super().get_queryset()


class ClientEditView(UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/edit_client.html'
    success_url = reverse_lazy('clients_list')


class ClientDeleteView(DeleteView):
    template_name = 'clients/delete_client.html'
    model = Client
    success_url = reverse_lazy('clients_list')
