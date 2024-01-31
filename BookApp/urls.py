# urls.py

from django.urls import path
from .views import AddBookView, ListAllBooksView, GetBookByIdView, AssignUpdateBookDetailsView

urlpatterns = [
    path('add', AddBookView.as_view(), name='add-book'),
    path('list', ListAllBooksView.as_view(), name='list-all-books'),
    path('get/<int:id>/', GetBookByIdView.as_view(), name='get-book-by-id'),
    path('update/<int:id>/', AssignUpdateBookDetailsView.as_view(), name='assign-update-book-details'),
]
