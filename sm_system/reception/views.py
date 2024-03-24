from django.shortcuts import render


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from sm_system.reception.models import ServiceOrder


class OrderCreateView(CreateView):
    model = ServiceOrder
    fields = '__all__'
    template_name = 'reception/create_order.html'
    success_url = 'orders_list'


class OrdersListView(ListView):
    model = ServiceOrder
    template_name = 'reception/orders_list.html'

    def get_queryset(self):
        return super().get_queryset()


class OrderEditView(UpdateView):
    model = ServiceOrder
    fields = '__all__'
    template_name = 'reception/edit_order.html'
    success_url = 'orders_list'


class OrderDeleteView(DeleteView):
    model = ServiceOrder
    template_name = 'reception/delete_order.html'
    success_url = reverse_lazy('orders_list')

class OrderDetailsView(DetailView):
    model = ServiceOrder
    template_name = 'reception/order_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
