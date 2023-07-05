from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from .serializers import AlbumSerializer, AddSongToAlbumSerializer, UserSongAlbumSerializer, PublicAlbumSerializer, UserFollowAlbumSerializer
from .models import Album, AlbumSong, Follower
from rest_framework.permissions import IsAuthenticated
from songs.permissions import CustomUserBasedPermission
from .filters import UserSongAlbumFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from songs.utils.pagination import CustomPagination
# Create your views here.


class AlbumView(ListCreateAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(user_id=user).order_by('id')

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except Exception as e:
            raise serializers.ValidationError({'message': e})


class AddSongToAlbumView(CreateAPIView):
    queryset = AlbumSong.objects.all()
    serializer_class = AddSongToAlbumSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]


class ListAlbumSongsView(ListAPIView):
    queryset = AlbumSong.objects.all().order_by('id')
    serializer_class = UserSongAlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserSongAlbumFilter
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]
    pagination_class = CustomPagination


class ListPublicAlbumView(ListAPIView):
    serializer_class = PublicAlbumSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(status='public').exclude(user_id=user).order_by('id')


class UserFollowAlbumView(ListCreateAPIView):
    serializer_class = UserFollowAlbumSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Follower.objects.filter(user_id=user).order_by('id')
