from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4),
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255, min_length=2)
    password = serializers.CharField(
        max_length=255, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']