from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Song
from .serializers import AddSongSerializer, SongSerializer
# Create your views here.


class SongCreateView(CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = AddSongSerializer


class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
