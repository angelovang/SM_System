from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from sm_system.clients.models import Client
from sm_system.reception.models import OrdersHistory, ServiceOrder
from tools.send_emails import send_email


@receiver(post_save, sender=OrdersHistory)
def order_history_created(sender, instance, **kwargs):
    if instance.completed or instance.price != 0:
        # Change service order status
        current_order = ServiceOrder.objects.filter(pk=instance.order_id).get()
        current_order.status = 'completed'
        current_order.save()

        # Take current client and then send email
        current_client = Client.objects.filter(pk=current_order.client_id).get()
        # Prepare send messages
        send_message = f'Order {current_order} is completed! End price is {instance.price} lv.'
        subject = f'Your order is completed ! From SM-system!'

        send_email(current_client, subject, send_message)

        return



