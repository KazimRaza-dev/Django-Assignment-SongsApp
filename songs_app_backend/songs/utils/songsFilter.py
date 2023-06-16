from songs.models import Song
import django_filters


class SongFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(
        field_name='tags__name', lookup_expr='icontains')

    class Meta:
        model = Song
        fields = ['title', 'tags']
