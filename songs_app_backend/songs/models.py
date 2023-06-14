from django.db import models
from taggit.managers import TaggableManager
from users.models import User
# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=100, unique=True)
    singer = models.CharField(max_length=100)
    tags = TaggableManager()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}({self.id})"


class UserSongLike(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='liked_songs')
    song_id = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name='liking_users')


class UserSongComment(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='songs_comments')
    song_id = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name='users_commented')
    comment = models.CharField(max_length=200)


class UserSongFavorite(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorite_songs')
    song_id = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name='users_favorited')


class Album(models.Model):
    ALBUM_STATUS_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public'),
    ]

    title = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=ALBUM_STATUS_CHOICES)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_albums")


class UserFollowAlbum(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed_albums')
    album_id = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name='users_following')


class UserSongAlbum(models.Model):
    song_id = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name='users_albums')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='songs_in_albums')
    album_id = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name='user_songs')
