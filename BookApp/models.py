from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    Published_date = models.DateField(auto_now=True)
    
class BookDetail(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    NumberOfPages = models.IntegerField()
    language = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    
class BorrowedBook(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date =  models.DateField()
    return_date =  models.DateField(null=True)