# Create your tasks here

from celery import shared_task
from .models import Song
from django.http import HttpResponseServerError


@shared_task
def add_song_task(validated_data):
    try:
        tags = validated_data.pop('tags', None)
        # Create the song instance
        song = Song.objects.create(**validated_data)
        # Add the tags on the song instance
        song.tags.add(*tags)
        print('New Song added successfully!')

    except Exception as e:
        return HttpResponseServerError({'message': 'Process to a Add new song failed.' + str(e)})
