from django.db import models
from users.models import User
from songs.models import Song
# Create your models here.


class Album(models.Model):
    ALBUM_STATUS_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public'),
    ]

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=ALBUM_STATUS_CHOICES)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_albums")

    class Meta:
        unique_together = ['title', 'user_id']


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

    class Meta:
        unique_together = ['album_id', 'song_id']
