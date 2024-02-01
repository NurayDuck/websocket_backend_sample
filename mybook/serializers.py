from rest_framework import serializers
from .models import Book, Payment, TelegramUser

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class PaymentSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer()
    class Meta:
        model = Payment
        fields = '__all__'



