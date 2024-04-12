from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from sm_system.reception.forms import OrderForm, RepairStartForm, HistoryStartForm, HistoryEndForm
from sm_system.reception.models import ServiceOrder, OrdersHistory


class OrderCreateView(auth_mixins.LoginRequiredMixin,CreateView):
    model = ServiceOrder
    form_class = OrderForm
    template_name = 'reception/create_order.html'
    success_url = reverse_lazy('orders_list')


class OrdersListView(auth_mixins.LoginRequiredMixin,ListView):
    model = ServiceOrder
    template_name = 'reception/orders_list.html'
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset()


class OrderEditView(auth_mixins.LoginRequiredMixin,UpdateView):
    model = ServiceOrder
    fields = '__all__'
    template_name = 'reception/edit_order.html'
    success_url = reverse_lazy('orders_list')


class OrderDeleteView(auth_mixins.LoginRequiredMixin,DeleteView):
    model = ServiceOrder
    template_name = 'reception/delete_order.html'
    success_url = reverse_lazy('orders_list')


class OrderDetailsView(auth_mixins.LoginRequiredMixin,DetailView):
    model = ServiceOrder
    template_name = 'reception/order_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SelectOrderView(auth_mixins.LoginRequiredMixin,ListView):
    model = ServiceOrder
    form_class = RepairStartForm
    template_name = 'reception/select_order.html'
    success_url = reverse_lazy('orders_list')
    paginate_by = 6
    def get_queryset(self):
        return super().get_queryset().filter(status='open')

@login_required
def start_repair(request, pk):
    order_id = pk
    current_user = request.user

    selected_order = ServiceOrder.objects.filter(pk=pk).get()
    selected_order.assign_to(technician=current_user)

    selected_order = ServiceOrder.objects.filter(pk=pk).get()
    order_history = OrdersHistory.objects.last()

    assigned_order_form = RepairStartForm(instance=selected_order)
    order_history_form = HistoryStartForm(instance=order_history)

    context = {
        'order_id': order_id,
        'history_id': order_history.id,
        'assigned_order_form': assigned_order_form,
        'order_history_form': order_history_form,
    }
    return render(request, 'reception/start_history.html', context)


class RepairsInProgressView(auth_mixins.LoginRequiredMixin,ListView):
    model = OrdersHistory
    template_name = 'reception/select_history.html'
    success_url = reverse_lazy('orders_list')
    paginate_by = 6
    def get_queryset(self):
        current_user_pk = self.request.user.pk
        return super().get_queryset().filter(technician=current_user_pk, resolution_description=None)


class EndRepairView(auth_mixins.LoginRequiredMixin,UpdateView):
    model = OrdersHistory
    form_class = HistoryEndForm
    template_name = 'reception/end_history.html'
    success_url = reverse_lazy('home_page')