from django.urls import path
from .views import UserRegistrationView, UserList, UserShow, UserLoginView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name = "register_user"),
    path('login', UserLoginView.as_view(), name ="login_user"),
    path('list', UserList.as_view()),
    path('view/<str:id>', UserShow.as_view(), name = "show_user"),
]