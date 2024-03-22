from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from sm_system.clients.models import Client


def clients_view(request):
    return render(request, 'clients/client_view.html')


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
