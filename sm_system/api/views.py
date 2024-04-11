from django.db.models import Q
from rest_framework.generics import ListAPIView
from sm_system.clients.models import Client
from .serializers import ClientSerializer


class APIClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



    # TODO: explain later (permissions are important for the project)
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()

        # TODO: explain what's happening here
        # TODO: explain the models.Q thing (powerful tool)
        _q = self.request.query_params.get('q', None)
        if _q is not None:
            queryset = queryset.filter(
                Q(first_name__startswith=_q)
                | Q(last_name__startswith=_q)
                | Q(phone_number__contains=_q)
                | Q(email__startswith=_q)
            )
        return queryset
