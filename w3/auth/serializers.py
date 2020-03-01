from .models import UserProfile, User
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    address = serializers.CharField(write_only=True, required=False)
    age = serializers.CharField(write_only=True, required=False)
    avatar = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = UserProfile
        fields = ('id', 'address', 'age', 'avatar')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'profile')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
