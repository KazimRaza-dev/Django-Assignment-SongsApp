from django.urls import path
from .views import SongCreateView, SongListView

urlpatterns = [
    path('', SongListView.as_view(), name='songs-list'),
    path('add/', SongCreateView.as_view(), name='add-song'),
]
