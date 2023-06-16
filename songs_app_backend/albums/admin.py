from django.contrib import admin
from .models import Album, UserFollowAlbum, UserSongAlbum
# Register your models here.


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'user_id')


@admin.register(UserFollowAlbum)
class UserFollowAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'album_id')


@admin.register(UserSongAlbum)
class UserSongAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id', 'album_id')
