from rest_framework import serializers

from datetime import datetime
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


class BorrowedBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['book', 'return_date']

    def create(self, validated_data):
        request = self.context['request'] 
        
        if BorrowedBook.objects.filter(user=request.user, book=validated_data['book'], return_date=None).exists():
            raise serializers.ValidationError('You have already borrowed this book and not returned it.')

        borrowed_book = BorrowedBook(
            book = validated_data['book'],
            borrow_date = datetime.now(),
            user = request.user,
        )
        borrowed_book.save()
        return borrowed_book
    
    def update(self, validated_data, id):
        request = self.context['request']

        borrowed_book = BorrowedBook.objects.filter(user=request.user, book=id)
        borrowed_book.return_date = datetime.now()
        borrowed_book.save()
        return borrowed_book
