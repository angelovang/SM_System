from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from sm_system.clients.models import Client
from sm_system.reception.models import ServiceOrder, OrdersHistory



def clients_view(request):
    return render(request, 'clients/client_view.html')



def client_order_info(request):
    search_code = request.GET.get('search2')

    try:
        current_order = ServiceOrder.objects.filter(so_id=search_code).get()
        current_history = OrdersHistory.objects.filter(order_id=current_order.pk).get()
    except:
        context = {'error': 'ERROR: You entered the wrong code or there is no such order !'}
        return render(request, 'clients/client_view.html', context)

    context = {
        'current_order': current_order,
        'current_history': current_history,
    }
    return render(request, 'clients/client_order_info.html', context)


class ClientCreateView(auth_mixins.LoginRequiredMixin, CreateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/create_client.html'
    success_url = reverse_lazy('clients_list')


class ClientListView(auth_mixins.LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/clients_list.html'
    paginate_by = 7

    def get_queryset(self):
        return super().get_queryset()


class ClientEditView(auth_mixins.LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/edit_client.html'
    success_url = reverse_lazy('clients_list')


class ClientDeleteView(auth_mixins.LoginRequiredMixin, DeleteView):
    template_name = 'clients/delete_client.html'
    model = Client
    success_url = reverse_lazy('clients_list')
