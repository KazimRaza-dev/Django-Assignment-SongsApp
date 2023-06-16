from django.urls import path
from .views import SongCreateView, SongListFilterView

urlpatterns = [
    path('', SongListFilterView.as_view(), name='songs-list-and-filter'),
    path('add/', SongCreateView.as_view(), name='add-song'),
]
