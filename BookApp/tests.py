from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Book, BookDetail
from .serializers import BookDetailSerializer

class BookTest(TestCase):
    def setUp(self):

        self.admin_user = get_user_model().objects.create_superuser(  
            email='admin@example.com',
            password = 'password'
        )
        
        self.book = Book(
            title='Test Book',
            ISBN='1234567890',
            genre='Fiction',
            
        )
        self.book.save()

        self.book_detail = BookDetail(
            book=self.book,
            NumberOfPages=200,
            language='English',
            publisher='Test Publisher'
        )
        self.book_detail.save()
       
        self.client = APIClient()


    def authenticate_admin_user(self): # becasue we have a custom authentication
        user_data = {
            'email': 'admin@example.com',
            'password':'password'
        }
        response = self.client.post('/api/user/login', user_data)
        token = response.data['token']
        self.header = {'HTTP_AUTH':f'Token {token}'}


    def test_create_book(self):
        self.authenticate_admin_user()
        
        new_book_data = {
            'title': 'Test book',
            'ISBN': '1234567890',
            'genre': 'Fiction',            
        }

        response = self.client.post('/api/book/add', new_book_data, **self.header)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], new_book_data['title'])
        self.assertEqual(response.data['ISBN'], new_book_data['ISBN'])
        self.assertEqual(response.data['genre'], new_book_data['genre'])
        self.bookid = response.data['id']
        print(self.bookid)


    def test_create_book_detail(self):
        
        self.authenticate_admin_user()

        new_book_detail_data = {
            'NumberOfPages': 250,
            'language': 'Spanish',
            'publisher': 'New Publisher'
        }

        response = self.client.post(f'/api/book/details/{self.book.id}/', new_book_detail_data, **self.header)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['NumberOfPages'], new_book_detail_data['NumberOfPages'])
        self.assertEqual(response.data['language'], new_book_detail_data['language'])
        self.assertEqual(response.data['publisher'], new_book_detail_data['publisher'])



    def test_update_book_detail(self):

        self.authenticate_admin_user()
   
        updated_book_detail_data = {
            'NumberOfPages': 300,
            'language': 'French',
            'publisher': 'Updated Publisher'
        }
        
        response = self.client.put(f'/api/book/details/{self.book.id}/', updated_book_detail_data, **self.header)
        self.assertEqual(response.status_code, 200)
        self.book_detail.refresh_from_db()
        self.assertEqual(self.book_detail.NumberOfPages, updated_book_detail_data['NumberOfPages'])
        self.assertEqual(self.book_detail.language, updated_book_detail_data['language'])
        self.assertEqual(self.book_detail.publisher, updated_book_detail_data['publisher'])
