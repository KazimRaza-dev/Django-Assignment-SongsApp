from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_min_length = 8

    class Meta:
        model = User
        fields = ('email', 'password', 'username',
                  'first_name', 'last_name', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, password):
        if len(password) < self.password_min_length:
            raise serializers.ValidationError(
                f'This password must contain at least {self.password_min_length} characters.')
        return password


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get(
                'request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError(
                    'Invalid email or password.')
        else:
            raise serializers.ValidationError(
                'Email and password are required.')

        data['user'] = user
        data['tokens'] = self.get_tokens(user)
        return data

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return {
            'access_token': access_token,
            'refresh_token': str(refresh),
        }
