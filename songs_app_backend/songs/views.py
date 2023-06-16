from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Song, UserSongLike, UserSongFavorite
from .serializers import AddSongSerializer, SongSerializer, LikeSongSerializer, FavoriteSongSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .utils.songsFilter import SongFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class SongCreateView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = AddSongSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.create(serializer.validated_data)
        return Response(response, status=201)


class SongListFilterView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SongFilter


class LikeSongView(CreateAPIView):
    queryset = UserSongLike.objects.all()
    serializer_class = LikeSongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class FavoriteSongView(CreateAPIView):
    queryset = UserSongFavorite.objects.all()
    serializer_class = FavoriteSongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
