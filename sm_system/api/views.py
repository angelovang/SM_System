from django.db.models import Q
from rest_framework.generics import ListAPIView
from sm_system.clients.models import Client
from .serializers import ClientSerializer
from django.contrib.auth import mixins as auth_mixins

class APIClientListView(auth_mixins.LoginRequiredMixin,ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        _q = self.request.query_params.get('q', None)
        if _q is not None:
            queryset = queryset.filter(
                Q(first_name__startswith=_q)
                | Q(last_name__startswith=_q)
                | Q(phone_number__contains=_q)
            )
        return queryset
