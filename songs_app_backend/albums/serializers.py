
from rest_framework import serializers
from .models import Album, UserSongAlbum


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = ['user_id']

    def create(self, validated_data):
        try:
            validated_data['user_id'] = self.context['request'].user
            return Album.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({'message': e})


class AddSongToAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSongAlbum
        exclude = ['user_id']

    def create(self, validated_data):
        try:
            user = self.context['request'].user
            album_id = self.context['request'].data.get('album_id')
            album = Album.objects.filter(id=album_id, user_id=user).first()

            if not album:
                raise serializers.ValidationError(
                    "You don't have permissions to add song to other users albums")

            validated_data['user_id'] = user
            return UserSongAlbum.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({'message': e})
