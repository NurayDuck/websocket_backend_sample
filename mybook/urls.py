from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:book_id>', views.BookAPIView.as_view()),
    path('api/payments/', views.PaymentAPIView.as_view()),
    # path('api/payments/<int:payment_id>', views.PaymentprocAPIView.as_view()) 
    
]
