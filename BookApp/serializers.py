from rest_framework import serializers
from .models import Book, BookDetail, BorrowedBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'ISBN', 'genre', 'Published_date']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = ['id', 'book', 'NumberOfPages', 'language', 'publisher']

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date']