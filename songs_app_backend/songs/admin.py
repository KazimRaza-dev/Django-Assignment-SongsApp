from django.contrib import admin
from .models import Song, UserSongLike, UserSongComment, UserSongFavorite, Album, UserSongAlbum, UserFollowAlbum
# Register your models here.


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'singer', 'tags', 'created_date')


@admin.register(UserSongLike)
class UserSongLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id')


@admin.register(UserSongFavorite)
class UserSongFavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id')


@admin.register(UserSongComment)
class UserSongCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id', 'comment')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'user_id')


@admin.register(UserFollowAlbum)
class UserFollowAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'album_id')


@admin.register(UserSongAlbum)
class UserSongAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id', 'album_id')
