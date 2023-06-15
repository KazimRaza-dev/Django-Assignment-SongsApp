from rest_framework import serializers
from .models import Song
from taggit.serializers import TagListSerializerField, TaggitSerializer


class AddSongSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Song
        fields = ('id', 'title', 'singer', 'tags')

    def create(self, validated_data):
        tags = validated_data.pop('tags', None)

        # Create the song instance
        song = Song.objects.create(**validated_data)

        # Add the tags on the song instance
        song.tags.add(*tags)
        return song


class SongSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Song
        fields = ('id', 'title', 'singer', 'tags')
