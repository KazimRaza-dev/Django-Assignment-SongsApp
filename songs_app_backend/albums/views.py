from rest_framework.generics import ListCreateAPIView
from .serializers import AlbumSerializer
from .models import Album
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from songs.utils.customPermissions import CustomUserBasedPermission
# Create your views here.


class AlbumView(ListCreateAPIView):
    serializer_class = AlbumSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(user_id=user)
