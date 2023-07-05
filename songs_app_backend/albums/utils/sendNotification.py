from albums.models import Album, Follower
from users.models import User
from songs.models import Song
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def sendNotificationToFollowersViaEmail(album_id, song_id):
    try:
        followers_emails = getAlbumFollowers(album_id)
        if not followers_emails:
            return 'No user is following this album.'

        message = Mail(
            from_email=os.getenv('EMAIL_SENDER'),
            to_emails=followers_emails,
            subject="New Song Added to Album You're Following " +
            str(datetime.now()),
            plain_text_content=getEmailBody(album_id, song_id)
        )
        sendgrid_client = SendGridAPIClient(
            api_key=os.getenv('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message)

        if response.status_code == 202:
            return 'Email sent successfully!'
        else:
            return 'Failed to send email'
    except Exception as e:
        return 'Exception occured ' + str(e)


def getAlbumFollowers(album_id):
    album_followers = Follower.objects.filter(
        album_id=album_id).values_list('user_id', flat=True)

    if not album_followers:
        return

    users_emails = User.objects.filter(
        id__in=album_followers).values_list('email', flat=True)
    # Convert user_ids to a list of strings
    return [str(email) for email in users_emails]


def getEmailBody(album_id, song_id):
    return "We are excited to inform you that a new song '" + \
        getSongTitle(song_id) + \
        "' has been added to the Album '" + getAlbumTitle(album_id) + "'."


def getAlbumTitle(album_id):
    album = Album.objects.get(id=album_id)
    return album.title


def getSongTitle(song_id):
    song = Song.objects.get(id=song_id)
    return song.title
