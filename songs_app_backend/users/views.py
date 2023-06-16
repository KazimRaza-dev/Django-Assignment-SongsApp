from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView

# Create your views here.


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            tokens = serializer.validated_data['tokens']
            return Response({'message': 'User successfully login', "token": tokens})
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
