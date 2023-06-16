from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Song
from .serializers import AddSongSerializer, SongSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .utils.songsFilter import SongFilter


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
