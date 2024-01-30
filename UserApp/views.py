from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserCreateSerializer, UsersSerializer, UserSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            token = user.token

            return Response({'user_id': user.id, 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class UserShow(generics.RetrieveAPIVIew):
    serializer = UserSerializer()
    queryset = User.objects.all()
