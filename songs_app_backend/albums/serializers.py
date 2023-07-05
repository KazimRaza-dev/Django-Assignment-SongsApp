
from rest_framework import serializers
from .models import Album, AlbumSong, Follower
from .utils.sendNotification import sendNotificationToFollowersViaEmail


class AlbumSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Album
        fields = '__all__'


class PublicAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'title', 'status', 'user_id')


class UserSongAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumSong
        fields = ('id', 'album_id', 'song_id', 'user_id')


class AddSongToAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumSong
        exclude = ['user_id']

    def create(self, validated_data):
        try:
            user = self.context['request'].user
            album_id = self.context['request'].data.get('album_id')
            song_id = self.context['request'].data.get('song_id')

            album = Album.objects.filter(id=album_id, user_id=user).first()
            if not album:
                raise serializers.ValidationError(
                    {'message': 'You do not have permissions to add song to other users albums'})

            validated_data['user_id'] = user
            # Sending notification to Album followers about new addition.
            sendNotificationToFollowersViaEmail(album_id, song_id)
            return AlbumSong.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({'message': e})


class UserFollowAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        exclude = ['user_id']

    def create(self, validated_data):
        try:
            validated_data['user_id'] = self.context['request'].user
            album_id = self.context['request'].data.get('album_id')
            album = Album.objects.filter(id=album_id, status='public').first()

            if not album:
                raise serializers.ValidationError(
                    {'message': 'Album Not Exists OR it is not Public.'})

            return Follower.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({'message': e})
