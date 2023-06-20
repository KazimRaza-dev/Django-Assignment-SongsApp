from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Song, UserSongLike, UserSongFavorite, UserSongComment
from .serializers import AddSongSerializer, SongSerializer, LikeSongSerializer, FavoriteSongSerializer, CommentOnSongSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .utils.songsFilter import SongFilter
from .utils.customPermissions import CustomUserBasedPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers


class SongListFilterView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SongFilter
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]


class SongCreateView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = AddSongSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response({"message": "Song creation scheduled successfully"}, status=201)


class LikeSongView(CreateAPIView):
    queryset = UserSongLike.objects.all()
    serializer_class = LikeSongSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except Exception as e:
            raise serializers.ValidationError(e)


class FavoriteSongView(CreateAPIView):
    queryset = UserSongFavorite.objects.all()
    serializer_class = FavoriteSongSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except Exception as e:
            raise serializers.ValidationError(e)


class CommentOnSongView(CreateAPIView):
    queryset = UserSongComment.objects.all()
    serializer_class = CommentOnSongSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except Exception as e:
            raise serializers.ValidationError(e)
