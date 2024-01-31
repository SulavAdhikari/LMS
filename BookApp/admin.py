from django.contrib import admin
from .models import Book, BookDetail, BorrowedBook
# Register your models here.


admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(BookDetail)
