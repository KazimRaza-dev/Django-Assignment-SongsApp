
from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = ['user_id']

    def create(self, validated_data):
        try:
            validated_data['user_id'] = self.context['request'].user
            return Album.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(e)
