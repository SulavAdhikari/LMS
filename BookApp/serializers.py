from rest_framework import serializers

from datetime import datetime
from .models import Book, BookDetail, BorrowedBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'ISBN', 'genre', 'Published_date']

class BookDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = BookDetail
        fields = ['id', 'book', 'NumberOfPages', 'language', 'publisher']

    def create(self, validated_data, id):
        book_detail = BookDetail(
            book=Book.objects.get(pk=id),
            NumberOfPages = validated_data["NumberOfPages"],
            publisher = validated_data["publisher"],
            language = validated_data['language']
        )
        book_detail.save()
        return book_detail

    def update(self, validated_data, id):
        instance = BookDetail.objects.all()
        bookdetail = instance.get(book=Book.objects.get(pk=id))
        if validated_data["NumberOfPages"]:
            bookdetail.NumberOfPages = validated_data['NumberOfPages']
        if validated_data['publisher']:
            bookdetail.publisher = validated_data['publisher']
        if validated_data['language']:
            bookdetail.language = validated_data['language']
        bookdetail.save()
        return bookdetail
    
        
class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date']


class BorrowedBookCreateSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    class Meta:
        model = BorrowedBook
        fields = ['book', 'return_date']
    lookup_field = 'id'
    def create(self, validated_data):
        id = self.context['view'].kwargs.get('id')
        request = self.context['request'] 
        
        if BorrowedBook.objects.filter(user=request.user, book=Book.objects.get(pk=id), return_date=None).exists():
            raise serializers.ValidationError('You have already borrowed this book and not returned it.')

        borrowed_book = BorrowedBook(
            book = Book.objects.get(pk=id),
            borrow_date = datetime.now(),
            user = request.user,
        )
        borrowed_book.save()
        return borrowed_book
    
    def update(self, validated_data, id):
        id = self.context['view'].kwargs.get('id')
        request = self.context['request']
        if not BorrowedBook.objects.filter(user=request.user, book=Book.objects.get(pk=id), return_date=None).exists():
            raise serializers.ValidationError('You have not borrowed this book.')

        borrowed_book = BorrowedBook.objects.filter(user=request.user, book=Book.objects.get(pk=id)).first()
        borrowed_book.return_date = datetime.today()
        borrowed_book.save()
        return borrowed_book
