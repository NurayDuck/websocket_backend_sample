from django.shortcuts import render

from rest_framework import generics
from .models import Book, Payment
from .serializers import BookSerializer, PaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['POST'])
# def create_payment(request):

#     user_id = request.data.get('user_id')
#     book_id = request.data.get('book_id')

#     if user_id is None or book_id is None:
#         return Response({'error': 'user_id and book_id are required'}, status=status.HTTP_400_BAD_REQUEST)

#     payment_data = {'user': user_id, 'book': book_id, 'status': 'not_processed'}
#     serializer = PaymentSerializer(data=payment_data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PaymentAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class BookAPIView(APIView):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            serialized_book = BookSerializer(book)  
            return Response(serialized_book.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Книга не найдена"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# class PaymentprocAPIView(APIView):
#     def get(self, request, payment_id):
#         try:
#             payment = Payment.objects.get(id=payment_id)
#             serialized_payment = PaymentSerializer(payment)  
#             return Response(serialized_payment.data, status=status.HTTP_200_OK)
#         except Payment.DoesNotExist:
#             return Response({"error": "Книга не найдена"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
