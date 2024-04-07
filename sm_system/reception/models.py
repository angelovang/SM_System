from datetime import date

from django.db import models

from sm_system.accounts.models import SmsUser
from sm_system.clients.models import Client
from tools.generate_id import generate_unique_id
from tools.last_client import last_client


class ServiceOrder(models.Model):
    ORDER_STATUS = (
        ('open', 'Open'),
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed')
    )

    DEVICE_TYPE = (
        ('computer', 'Computer'),
        ('laptop', 'Laptop'),
        ('monitor', 'Monitor'),
        ('printer', 'Printer')
    )

    SK_MAX_LEN = 20
    DEVICE_TYPE_MAX_LEN = 20
    DEVICE_DATA_MAX_LEN = 200
    PRICE_MAX_LENGTH = 10
    ISSUE_MAX_LEN = 300
    RESOLUTION_MAX_LEN = 300
    STATUS_MAX_LEN = 20

    so_id = models.CharField(
        max_length=SK_MAX_LEN,
        unique=True,
        default=generate_unique_id,
        editable=False,
    )

    accept_date = models.DateField(
        blank=False,
        null=False,
        default=date.today,
    )

    close_date = models.DateField(
        blank=True,
        null=True,
        default=date.today
    )

    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=False, blank=False, default=last_client())

    technician = models.ForeignKey(SmsUser, on_delete=models.DO_NOTHING, null=True, blank=True)

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
        max_length=ISSUE_MAX_LEN,
    )

    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=ORDER_STATUS,
        default='Open',
    )

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.id}--{self.client}--{self.device_type}--{self.issue_description}'

    def assign_to(self, technician):
        self.technician = technician

        if self.status == 'open':
            self.status = "in_progress"

        # Order history create
        current_status = OrdersHistory.objects.filter(order_id=self.id)
        print (current_status)
        if not current_status:
            OrdersHistory.objects.create(
                order=self,
                technician=technician,
            )
            self.save()
            return
        # TO DO: Kakwo prawim ako we4e ima takyw zapis ?
        # else:
        #     return Exception('This order has already been started')


class OrdersHistory(models.Model):
    order = models.ForeignKey(ServiceOrder, on_delete=models.DO_NOTHING)
    technician = models.ForeignKey(SmsUser, on_delete=models.DO_NOTHING, null=True, blank=True)

    start_date = models.DateField(
        default=date.today,
        null=False,
        blank=False,
    )

    date_of_complete = models.DateField(
        default=date.today,
        null=True,
        blank=True,
    )

    resolution_description = models.TextField(
        default=None,
        null=True,
        blank=True,
    )

    price = models.FloatField(
        default=0.00,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.id}--{self.order}--{self.start_date}'
