from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from sm_system.clients.forms import ClientForm
from sm_system.reception.forms import OrderForm, HistoryStartForm
from sm_system.reception.models import ServiceOrder, OrdersHistory


def order_create(request):
    global client
    client_saved = False
    order_saved = False

    if request.method == 'GET':
        client = ClientForm()
        order = OrderForm()
    else:
        if not client_saved:
            client = ClientForm(request.POST)
            if client.is_valid():
                order = OrderForm()
                client.save()
                client_saved = True

                client_context = {
                    'client': client,
                    'order': order,
                    'client_saved': client_saved
                }
                return render(request, 'reception/create_order.html', client_context)

        order = OrderForm(request.POST)
        if order.is_valid():
            order.save()
            order_saved = True
            order_context = {
                'client': client,
                'order': order,
                'order_saved': order_saved
            }
            #return redirect('orders_list')
            return render(request, 'reception/create_order.html', order_context)

    context = {
        'client': client,
        'order': order,
        'client_saved': client_saved,
        'order_saved': order_saved
    }
    return render(request, 'reception/create_order.html', context)


# class OrderCreateView(CreateView):
#     model = ServiceOrder
#     form_class = OrderForm
#     template_name = 'reception/create_order.html'
#     success_url = reverse_lazy('orders_list')


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


class StartRepairView(ListView):
    model = ServiceOrder
    form_class= HistoryStartForm
    template_name = 'reception/start_history.html'
    success_url = reverse_lazy('orders_list')

    def get_queryset(self):
        return super().get_queryset().filter(status='open')

class EndRepairView(UpdateView):
    model = OrdersHistory
    # form_class =
    template_name = 'reception/end_history.html'
    success_url = reverse_lazy('home_page')