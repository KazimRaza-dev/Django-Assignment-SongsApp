from django.urls import path
from .views import SongCreateView, SongListFilterView, LikeSongView, FavoriteSongView

urlpatterns = [
    path('', SongListFilterView.as_view(), name='songs-list-and-filter'),
    path('add/', SongCreateView.as_view(), name='add-song'),
    path('like/', LikeSongView.as_view(), name='like-song'),
    path('favorite/', FavoriteSongView.as_view(), name='add-song-to-favorite'),

]
