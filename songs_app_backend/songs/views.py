from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Song
from .serializers import AddSongSerializer, SongSerializer
from rest_framework.response import Response


class SongCreateView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = AddSongSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.create(serializer.validated_data)
        return Response(response, status=201)


class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
