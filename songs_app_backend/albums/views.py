from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from .serializers import AlbumSerializer, AddSongToAlbumSerializer, UserSongAlbumSerializer, PublicAlbumSerializer, UserFollowAlbumSerializer
from .models import Album, AlbumSong, Follower
from rest_framework.permissions import IsAuthenticated
from songs.permissions import CustomUserBasedPermission
from .filters import UserSongAlbumFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
# Create your views here.


class AlbumView(ListCreateAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(user_id=user)

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except Exception as e:
            raise serializers.ValidationError({'message': e})


class AddSongToAlbumView(CreateAPIView):
    queryset = AlbumSong.objects.all()
    serializer_class = AddSongToAlbumSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]


class ListUserAlbumSongsView(ListAPIView):
    queryset = AlbumSong.objects.all()
    serializer_class = UserSongAlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserSongAlbumFilter
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]


class ListPublicAlbumView(ListAPIView):
    serializer_class = PublicAlbumSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(status='public').exclude(user_id=user)


class UserFollowAlbumView(ListCreateAPIView):
    serializer_class = UserFollowAlbumSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def get_queryset(self):
        user = self.request.user
        return Follower.objects.filter(user_id=user)
