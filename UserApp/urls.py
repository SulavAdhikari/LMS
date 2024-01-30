from django.urls import path
from .views import UserRegistrationView, UserList, UserShow

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name = "register_user"),
    path('list', UserList.as_view()),
    path('view/<str:id>', UserShow.as_view(), name = "show_user"),
]