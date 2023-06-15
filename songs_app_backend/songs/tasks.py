# Create your tasks here

from celery import shared_task
from .models import Song


@shared_task
def add_song_task(validated_data):
    try:
        tags = validated_data.pop('tags', None)
        # Create the song instance
        song = Song.objects.create(**validated_data)
        # Add the tags on the song instance
        song.tags.add(*tags)
        print(song)
        print("New Song added successfully!")

    except Exception as e:
        print(e)
        print('Process to a new song failed.')
