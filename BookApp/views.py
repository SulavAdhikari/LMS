from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Book, BookDetail, BorrowedBook
from .serializers import BookSerializer, BookDetailSerializer, BorrowedBookCreateSerializer, BorrowedBookSerializer
from UserApp.authentication import CustomJWTAuthentication
from datetime import datetime


class AddBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [CustomJWTAuthentication]



class ListAllBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class GetBookByIdView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'



class AssignUpdateBookDetailsView(generics.UpdateAPIView):
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [CustomJWTAuthentication]



class BorrowBookView(generics.CreateAPIView):
    
    serializer_class = BorrowedBookCreateSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


class ReturnBookView(generics.UpdateAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookCreateSerializer
    lookup_field = 'id'
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListAllBorrowedBooksView(generics.ListAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BorrowedBook.objects.filter(user=user)