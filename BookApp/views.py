from rest_framework import generics
from .models import Book, BookDetail, BorrowedBook
from .serializers import BookSerializer, BookDetailSerializer, BorrowedBookSerializer

class AddBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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

