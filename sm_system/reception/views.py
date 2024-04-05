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
    user = request.user
    selected_order = ServiceOrder.objects.filter(pk=pk).values()[0]
    selected_order['technician']= user
    print(selected_order)
    print(user)
    
    if request.method == 'POST':
        select_form = RepairStartForm(request.POST)
        history_form = HistoryForm(request.POST)
        if select_form.is_valid() and history_form.is_valid():
            select_form.save()
            history_form.save()
    
    else:
        select_form = RepairStartForm(initial=selected_order)
        history_form = HistoryForm(initial={'order':selected_order})

    context = {
        'select_form': select_form,
        'history_form': history_form,
    }
    return render(request, 'reception/start_history.html', context)



class EndRepairView(UpdateView):
    model = OrdersHistory
    # form_class =
    template_name = 'reception/end_history.html'
    success_url = reverse_lazy('home_page')