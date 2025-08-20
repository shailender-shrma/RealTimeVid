from django.db import models
from hls.models import VideoFileField

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = VideoFileField(upload_to='videos/hls', format='mp4')