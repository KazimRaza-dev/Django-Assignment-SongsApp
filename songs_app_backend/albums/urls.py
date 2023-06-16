from django.urls import path
from .views import AlbumView, AddSongToAlbumView

urlpatterns = [
    path('', AlbumView.as_view(), name='create-list-album'),
    path('add/', AddSongToAlbumView.as_view(), name='add-song-to-album'),

]
