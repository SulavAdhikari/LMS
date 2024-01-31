from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth import authenticate
from .serializers import UserCreateSerializer, UsersSerializer, UserSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            token = user.token

            return Response({'user_id': user.id, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class UserShow(generics.RetrieveAPIView):
    serializer = UserSerializer()
    queryset = User.objects.all()

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token = user.token

            return Response({'user_id': user.id, 'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)