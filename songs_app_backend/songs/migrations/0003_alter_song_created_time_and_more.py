# Generated by Django 4.2.2 on 2023-06-16 06:45

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0002_remove_song_created_date_song_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 16, 6, 45, 15, 891499)),
        ),
        migrations.AlterUniqueTogether(
            name='usersonglike',
            unique_together={('user_id', 'song_id')},
        ),
    ]