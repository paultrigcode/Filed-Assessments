from rest_framework import serializers
from .models import Song,Podcast,Audiobook

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name','duration_in_number_of_seconds','uploaded_time']

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['id', 'name','duration_in_number_of_seconds','uploaded_time','host','participant']


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = ['id', 'title','author','narrator','duration_in_number_of_seconds','uploaded_time']