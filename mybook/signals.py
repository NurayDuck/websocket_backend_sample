from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Payment
from . import consumers

@receiver(post_save, sender=Payment)
def send_payment_status_update(sender, instance, **kwargs):
    payment_consumer = consumers.PaymentConsumer()
    # payment_consumer.payment_status_update()
    if instance.status == 'processed':
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'payment_group',
            {
                'type': 'payment_status_update',
                'payment_id': instance.id,
                'user_id': instance.user.telegram_id,
            }
        )
