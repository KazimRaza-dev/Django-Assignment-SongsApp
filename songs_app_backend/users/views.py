from django.shortcuts import render
from .serializer import UserRegistrationSerializer, UserLoginSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserLoginView(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = self.get_tokens(user)
            return Response({'message': 'User successfully login', "token": tokens})
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return {
            'access_token': access_token,
            'refresh_token': str(refresh),
        }
