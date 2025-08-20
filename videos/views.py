from django.shortcuts import render
from .models import Video


def video_stream(request):
    videos = Video.objects.all()
    return render(request, 'videos/video_stream.html', {'videos': videos})