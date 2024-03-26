from sm_system.clients.models import Client


def last_client():
    clients = Client.objects.all()
    last = clients[::]
    return last