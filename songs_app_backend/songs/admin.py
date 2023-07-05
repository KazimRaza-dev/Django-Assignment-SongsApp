from django.contrib import admin
from .models import Song, Like, Comment, Favorite


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'singer',
                    'tag_list', 'created_time',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class LikeSongAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id')


class FavoriteSongAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id')


class CommentSongAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'song_id', 'comment')


admin.site.register(Song, SongAdmin)
admin.site.register(Like, LikeSongAdmin)
admin.site.register(Favorite, FavoriteSongAdmin)
admin.site.register(Comment, CommentSongAdmin)
