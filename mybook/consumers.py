import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Payment, Book, TelegramUser

class PaymentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        await self.channel_layer.group_add(
            'payment_group',
            self.channel_name
        )


    async def disconnect(self, close_code):
        # Удаление из группы при отключении клиента
        await self.channel_layer.group_discard(
            'payment_group',
            self.channel_name
        )


    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            telegram_user_id = data.get('user')
            book_id = data.get('id')
            print(text_data)

            if telegram_user_id and book_id:
                telegram_user, created = await database_sync_to_async(TelegramUser.objects.get_or_create)(
                    telegram_id=telegram_user_id
                )

                book = await database_sync_to_async(Book.objects.get)(id=book_id)

                payment = await database_sync_to_async(Payment.objects.create)(
                    user=telegram_user,
                    book=book,
                    status='not_processed'
                )


                response_data = {
                    'action': 'payment_created',
                    'payment_id': payment.id,
                    'user': telegram_user_id,
                    'book_id': book_id,
                }
                await self.send(text_data=json.dumps(response_data))

        except json.JSONDecodeError:
            print("Invalid JSON format")

    async def payment_status_update(self, event):
        # Отправка обновлений статуса оплаты клиентам в группе
        print("ASDASDASD: ", event)
        payment_id = event.get("payment_id")
        user_id = event.get("user_id")
        print("ergee")
        response_data = {
            'action': 'payment_status_update',
            'payment_id': payment_id,
            'user_id': user_id
        }

        await self.send(text_data=json.dumps(response_data))
