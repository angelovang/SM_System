from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from sm_system.clients.models import Client
from sm_system.reception.models import OrdersHistory, ServiceOrder


@receiver(post_save, sender=OrdersHistory)
def order_history_created(sender, instance, **kwargs):
    if instance.completed or instance.price != 0:
        print(f'History order completed!!!')
        # Change service order status
        current_order = ServiceOrder.objects.filter(pk=instance.order_id).get()
        current_order.status = 'completed'
        current_order.save()

        # Take current client and then his email
        current_client = Client.objects.filter(pk=current_order.client_id).get()
        current_email = current_client.email

        # Prepare send message
        send_message = f'Order {current_order} is completed! End price is {instance.price} lv.'

        send_mail(
            subject='Your order is completed ! From SM-system!',
            message=send_message,
            from_email='info@sm_system.com',
            recipient_list=('angelovang55@gmail.com',current_email,)
        )

        return
