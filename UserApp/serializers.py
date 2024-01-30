from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'email', 'password')
        model = get_user_model()
        
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = get_user_model()