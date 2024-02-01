from django.contrib import admin
from .models import Book, Payment, TelegramUser

admin.site.register(Book)
admin.site.register(Payment)
admin.site.register(TelegramUser)
