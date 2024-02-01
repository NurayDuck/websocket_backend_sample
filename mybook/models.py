from django.db import models

class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=255, unique=True)

class Book(models.Model):
    bookname=models.CharField(max_length=255)

    author=models.CharField(max_length=255)

    number_of_pages=models.IntegerField()

    price=models.IntegerField(null=True)

    def __str__(self):
        return self.bookname
    
from django.contrib.auth.models import User

class Payment(models.Model):
    PROCESSED_CHOICES = [
        ('processed', 'Processed'),
        ('not_processed', 'Not Processed'),
    ]

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, null=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    
    status = models.CharField(max_length=20, choices=PROCESSED_CHOICES, default='not_processed')

