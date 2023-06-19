import django_filters
from albums.models import UserSongAlbum


class UserSongAlbumFilter(django_filters.FilterSet):
    # Define the filters based on the query string parameters you want to use
    name = django_filters.CharFilter(
        field_name='album_id__song_id_user_id', lookup_expr='icontains')

    class Meta:
        model = UserSongAlbum
        fields = ['album_id', 'song_id', 'user_id']
