from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from .serializers import AlbumSerializer, AddSongToAlbumSerializer, UserSongAlbumSerializer, PublicAlbumSerializer, UserFollowAlbumSerializer
from .models import Album, UserSongAlbum, UserFollowAlbum
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from songs.utils.customPermissions import CustomUserBasedPermission
from .utils.albumFilters import UserSongAlbumFilter
from django_filters.rest_framework import DjangoFilterBackend

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


class ListUserAlbumSongsView(ListAPIView):
    queryset = UserSongAlbum.objects.all()
    serializer_class = UserSongAlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserSongAlbumFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]


class ListPublicAlbumView(ListAPIView):
    serializer_class = PublicAlbumSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(status='public').exclude(user_id=user)


class UserFollowAlbumView(ListCreateAPIView):
    serializer_class = UserFollowAlbumSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def get_queryset(self):
        user = self.request.user
        return UserFollowAlbum.objects.filter(user_id=user)
