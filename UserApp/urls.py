from django.urls import path
from .views import UserRegistrationView, UserList, UserShow

urlpatterns = [
    path('register', UserRegistrationView, name = "register_user"),
    path('list', UserList),
    path('view/<str:id>', UserShow, name = "show_user"),
]