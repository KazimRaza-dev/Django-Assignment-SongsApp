from django.contrib import admin
from .models import Album, Follower, AlbumSong


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'user_id')


class AlbumFollowersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'album_id')


class AlbumSongsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id', 'album_id')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Follower, AlbumFollowersAdmin)
admin.site.register(AlbumSong, AlbumSongsAdmin)
