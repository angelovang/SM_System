from django.db import models

from sm_system.accounts.models import SmsUser
from sm_system.clients.models import Client
from tools.generate_id import generate_unique_id

ORDER_STATUS = {
    'open': 'Open',
    'in_progress': 'In progress',
    'completed': 'Completed',
    'closed': 'Closed'
}

DEVICE_TYPE = {
    'computer': 'Computer',
    'laptop': 'Laptop',
    'monitor': 'Monitor',
    'printer': 'Printer'
}


class ServiceOrder(models.Model):
    SK_MAX_LEN = 8
    DEVICE_TYPE_MAX_LEN = 20
    DEVICE_DATA_MAX_LEN = 200
    PRICE_MAX_LENGTH = 10
    ISSUE_MAX_LEN = 300
    RESOLUTION_MAX_LEN = 300
    STATUS_MAX_LEN = 20

    so_id = models.CharField(
        max_length=SK_MAX_LEN,
        unique=True,
        default=generate_unique_id(),
        editable=False,
    )

    so_pass = models.CharField(
        max_length=SK_MAX_LEN,
        unique=True,
        default=generate_unique_id(),
        editable=False,
    )

    accept_date = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False, blank=False)

    technician = models.ForeignKey(SmsUser, on_delete=models.CASCADE, null=True, blank=True)

    device_type = models.CharField(
        max_length=DEVICE_TYPE_MAX_LEN,
        choices=DEVICE_TYPE,
        null=False,
        blank=False,

    )

    device_data = models.CharField(
        max_length=DEVICE_DATA_MAX_LEN,
        null=False,
        blank=False,
    )

    issue_description = models.TextField(
        max_length = ISSUE_MAX_LEN,
    )

    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=ORDER_STATUS,
    )

    class Meta:
        ordering = ('-pk',)


class ServiceOrderHistory(models.Model):
    order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE)
    technician = models.ForeignKey(SmsUser, on_delete=models.CASCADE, null=True, blank=True)

    date_of_complete = models.DateField(
        auto_now=True,
        blank=True,
        null=True,
    )

    resolution_description = models.TextField()

    price = models.FloatField(
        default= 0.00,
        null=False,
        blank=False,
    )




