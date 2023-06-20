from django.contrib import admin
from .models import Song, UserSongLike, UserSongComment, UserSongFavorite, Album, UserSongAlbum, UserFollowAlbum
# Register your models here.


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'singer',
                    'tag_list', 'created_time',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class UserSongLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id')


class UserSongFavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id')


class UserSongCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id', 'comment')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'user_id')


class UserFollowAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'album_id')


class UserSongAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id', 'album_id')


admin.site.register(Song, SongAdmin)
admin.site.register(UserSongLike, UserSongLikeAdmin)
admin.site.register(UserSongFavorite, UserSongFavoriteAdmin)
admin.site.register(UserSongComment, UserSongCommentAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(UserFollowAlbum, UserFollowAlbumAdmin)
admin.site.register(UserSongAlbum, UserSongAlbumAdmin)
