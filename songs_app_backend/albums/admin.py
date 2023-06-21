from django.contrib import admin
from .models import Album, UserFollowAlbum, UserSongAlbum


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'user_id')


class UserFollowAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'album_id')


class UserSongAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id', 'album_id')


admin.site.register(Album, AlbumAdmin)
admin.site.register(UserFollowAlbum, UserFollowAlbumAdmin)
admin.site.register(UserSongAlbum, UserSongAlbumAdmin)
