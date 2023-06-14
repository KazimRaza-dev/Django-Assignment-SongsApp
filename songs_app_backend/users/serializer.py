from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_min_length = 8

    class Meta:
        model = User
        fields = ('email', 'password', 'username',
                  'first_name', 'last_name', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True},
            # 'first_name': {'required': True},
            # 'last_name': {'required': True}
        }

    def validate_password(self, password):
        if len(password) < self.password_min_length:
            raise serializers.ValidationError(
                f'This password must contain at least {self.password_min_length} characters.')
        return password

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


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
        return data
