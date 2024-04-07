from django.forms import forms
from django.http import JsonResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from sm_system.reception.forms import OrderForm, RepairStartForm, HistoryForm
from sm_system.reception.models import ServiceOrder, OrdersHistory


class OrderCreateView(CreateView):
    model = ServiceOrder
    form_class = OrderForm
    template_name = 'reception/create_order.html'
    success_url = reverse_lazy('orders_list')


class OrdersListView(ListView):
    model = ServiceOrder
    template_name = 'reception/orders_list.html'

    def get_queryset(self):
        return super().get_queryset()


class OrderEditView(UpdateView):
    model = ServiceOrder
    fields = '__all__'
    template_name = 'reception/edit_order.html'
    success_url = reverse_lazy('orders_list')


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


class SelectOrderView(ListView):
    model = ServiceOrder
    form_class= RepairStartForm
    template_name = 'reception/select_order.html'
    success_url = reverse_lazy('orders_list')

    def get_queryset(self):
        return super().get_queryset().filter(status='open')


def start_repair(request, pk):
    order_id = pk
    current_user = request.user
    selected_order = ServiceOrder.objects.filter(pk=pk).get()
    selected_order.assign_to(technician=current_user)
    selected_order = ServiceOrder.objects.filter(pk=pk).get()
    order_history = OrdersHistory.objects.last()

    #history_id = order_history.last()

    assigned_order_form = RepairStartForm(instance=selected_order)
    order_history_form = HistoryForm(instance=order_history)

    context = {
        'order_id': order_id,
        'history_id': order_history.id,
        'assigned_order_form': assigned_order_form,
        'order_history_form': order_history_form,
    }
    return render(request, 'reception/start_history.html', context)

def repair_started(request):
    pass

class EndRepairView(UpdateView):
    model = OrdersHistory
    # form_class =
    template_name = 'reception/end_history.html'
    success_url = reverse_lazy('home_page')