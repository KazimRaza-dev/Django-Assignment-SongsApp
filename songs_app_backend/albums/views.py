from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .serializers import AlbumSerializer, AddSongToAlbumSerializer
from .models import Album, UserSongAlbum
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


class AddSongToAlbumView(CreateAPIView):
    queryset = UserSongAlbum.objects.all()
    serializer_class = AddSongToAlbumSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]
