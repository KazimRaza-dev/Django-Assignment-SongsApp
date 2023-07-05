from rest_framework import serializers
from .models import Song, Like, Favorite, Comment
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .tasks import add_song_task
from datetime import datetime, timedelta
import pytz


class SongSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Song
        fields = ('id', 'title', 'singer', 'tags')


class AddSongSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Song
        fields = ('id', 'title', 'singer', 'tags', 'created_time')
        extra_kwargs = {
            'created_time': {'required': True}
        }

    def validate(self, data):
        scheduled_time = data.get('created_time')
        schedule_datetime = scheduled_time.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Get the current time in Pakistan Standard Time (PST)
        pst_timezone = pytz.timezone('Asia/Karachi')
        current_time = datetime.now(
            pst_timezone).strftime("%Y-%m-%dT%H:%M:%SZ")

        # Check if the scheduled time is in the future
        if schedule_datetime <= current_time:
            raise serializers.ValidationError(
                'Scheduled time must be in the future.')

        data['creation_time'] = self.calculate_creation_time_seconds(
            schedule_datetime, current_time)
        return data

    def create(self, validated_data):
        creation_time_seconds = validated_data.pop(
            'creation_time', None)

        # Schedule the Celery task to execute after the time difference in seconds
        add_song_task.apply_async(
            args=(validated_data,),
            eta=creation_time_seconds
        )

    def calculate_creation_time_seconds(self, schedule_datetime, current_time):
        # Convert the schedule and current time strings to datetime objects
        schedule = datetime.strptime(schedule_datetime, "%Y-%m-%dT%H:%M:%SZ")
        current = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%SZ")

        # Calculate the time difference between the scheduled time and the current time
        time_difference = schedule - current

        # Convert the time difference to seconds
        time_difference_seconds = time_difference.total_seconds()
        # print("Time difference in seconds: ", time_difference_seconds)

        desired_time_seconds = datetime.now() + timedelta(seconds=time_difference_seconds)
        return desired_time_seconds


class LikeSongSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'


class FavoriteSongSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Favorite
        fields = '__all__'


class CommentOnSongSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
