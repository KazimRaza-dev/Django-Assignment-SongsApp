from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Song, Like, Favorite, Comment
from .serializers import AddSongSerializer, SongSerializer, LikeSongSerializer, FavoriteSongSerializer, CommentOnSongSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SongFilter
from .permissions import CustomUserBasedPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from .utils.pagination import CustomPagination


class SongListFilterView(ListAPIView):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SongFilter
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]
    pagination_class = CustomPagination


class SongCreateView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = AddSongSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response({'message': 'Song creation scheduled successfully'}, status=201)


class LikeSongView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSongSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except Exception as e:
            raise serializers.ValidationError({'message': e})


class FavoriteSongView(CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSongSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except Exception as e:
            raise serializers.ValidationError({'message': e})


class CommentOnSongView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentOnSongSerializer
    permission_classes = [IsAuthenticated, CustomUserBasedPermission]

    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except Exception as e:
            raise serializers.ValidationError({'message': e})
