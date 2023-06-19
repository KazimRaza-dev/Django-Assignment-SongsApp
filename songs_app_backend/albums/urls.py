from django.urls import path
from .views import AlbumView, AddSongToAlbumView, ListUserAlbumSongsView, ListPublicAlbumView, UserFollowAlbumView

urlpatterns = [
    path('', AlbumView.as_view(), name='create-list-album'),
    path('add/', AddSongToAlbumView.as_view(), name='add-song-to-album'),
    path('filter/', ListUserAlbumSongsView.as_view(),
         name='filter-by-albums-users-songs'),
    path('public/', ListPublicAlbumView.as_view(), name='list-public-album'),
    path('follow/', UserFollowAlbumView.as_view(),
         name='follow-list-public-album'),

]
