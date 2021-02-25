from django.shortcuts import render
from crudapi.models import Song,Podcast,Audiobook
from crudapi.serializers import SongSerializer,PodcastSerializer,AudiobookSerializer
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.views import APIView
from cerberus import Validator
from django.core.exceptions import ObjectDoesNotExist


class AudioView(APIView):
    schema1 = {
        'name': {'type': 'string'},
        'duration':{'type':'integer'},
        'audioFileType':{'type':'string'}
    }
    schema2 = {
        'name': {'type': 'string'},
        'duration':{'type':'integer'},
        'audioFileType':{'type':'string'},
        'host':{'type':'string'},
        'participant':{'type':'list','required': False}
    }
    schema3 = {
        'title': {'type': 'string'},
        'duration':{'type':'integer'},
        'audioFileType':{'type':'string'},
        'author':{'type':'string'},
        'narrator':{'type':'string'}

    }
    
    def delete(self,request,pk,slug):
        if slug == "Song":
            try:
                song = Song.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Song with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            Song.objects.filter(id =pk).delete()
            return Response({
                "status": "success",
            })
        elif slug == "Podcast":
            try:
                podcast = Podcast.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Podcast with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
            Podcast.objects.filter(id =pk).delete()
            return Response({
                "status": "success",
            })
        elif slug == "Audiobook":
            try:
                audiobook = Audiobook.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Audiobook with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
            Audiobook.objects.filter(id =pk).delete()
            return Response({
                "status": "success",
            })
        return Response({
                "errors": "Invalid   audioFileType. audioFileType can either be Song,Podcast or Audiobook "
            }, status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        file_type = request.data["audioFileType"]
        if file_type == "Song":
            v = Validator(self.schema1)
            v.require_all = True
            if not v.validate(request.data):
                return Response({
                    "errors": v.errors
                }, status.HTTP_400_BAD_REQUEST)
            name = request.data["name"]
            duration = request.data['duration']
            song = Song.objects.create(name = name,duration_in_number_of_seconds = duration)
            return Response({
                "status": "success",
                "data": model_to_dict(song)
            })

        elif file_type == "Podcast":
            v = Validator(self.schema2)
            v.require_all = True
            if not v.validate(request.data):
                return Response({
                    "errors": v.errors
                }, status.HTTP_400_BAD_REQUEST)
            name = request.data["name"]
            duration = request.data['duration']
            host = request.data['host']
            if "participant" in request.data:
                participant = request.data['participant']
                podcast = Podcast.objects.create(name = name,duration_in_number_of_seconds = duration, host =host,participant =participant)
            else:
                podcast = Podcast.objects.create(name = name,duration_in_number_of_seconds = duration, host =host)

            return Response({
                "status": "success",
                "data": model_to_dict(podcast)
            })
        elif file_type == "Audiobook":
            v = Validator(self.schema3)
            v.require_all = True
            if not v.validate(request.data):
                return Response({
                    "errors": v.errors
                }, status.HTTP_400_BAD_REQUEST)
            title = request.data["title"]
            author = request.data["author"]
            narrator = request.data["narrator"]
            duration = request.data['duration']
            audiobook = Audiobook.objects.create(title = title,duration_in_number_of_seconds = duration, author = author,narrator = narrator)
            return Response({
                "status": "success",
                "data": model_to_dict(audiobook)
            })

        else:
             return Response({
                "errors": "Invalid   audioFileType. audioFileType can either be Song,Podcast or Audiobook "
            }, status.HTTP_400_BAD_REQUEST)


    def put(self,request,slug,pk):
        if slug == "Song":
            print(request.data)
            try:
                song = Song.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Song with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
            v = Validator(self.schema1)
            v.require_all = True
            if not v.validate(request.data):
                return Response({
                    "errors": v.errors
                }, status.HTTP_400_BAD_REQUEST)
            name = request.data["name"]
            duration = request.data['duration']
            song = Song.objects.get(pk=pk)
            song.name = name
            song.duration_in_number_of_seconds =duration
            song.save()
            return Response({
                "status": "success",
                "data": model_to_dict(song)

            })

        elif slug == "Audiobook":
            try:
                audiobook = Audiobook.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Audiobook with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
            v = Validator(self.schema3)
            v.require_all = True
            if not v.validate(request.data):
                return Response({
                    "errors": v.errors
                }, status.HTTP_400_BAD_REQUEST)
            title = request.data["title"]
            author = request.data["author"]
            narrator = request.data["narrator"]
            duration = request.data['duration']
            audiobook = Audiobook.objects.get(pk=pk)
            audiobook.title = title
            audiobook.author = author
            audiobook.narrator = narrator
            audiobook.duration_in_number_of_seconds= duration
            audiobook.save()
            return Response({
                "status": "success",
                "data": model_to_dict(audiobook)

            })

        elif slug == "Podcast":
            try:
                podcast = Podcast.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Podcast with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
            v = Validator(self.schema2)
            v.require_all = True
            if not v.validate(request.data):
                return Response({
                    "errors": v.errors
                }, status.HTTP_400_BAD_REQUEST)
            name = request.data["name"]
            duration = request.data['duration']
            host = request.data['host']
            if "participant" in request.data:
                participant = request.data['participant']
            podcast = Podcast.objects.get(pk=pk)
            podcast.name = name
            podcast.duration_in_number_of_seconds =duration
            podcast.host = host
            if "participant" in request.data:
                podcast.participant =participant
            podcast.save()
            return Response({
                "status": "success",
                "data": model_to_dict(podcast)

            })
        else:
            return Response({
                "errors": "Invalid   audioFileType. audioFileType can either be Song,Podcast or Audiobook "
            }, status.HTTP_400_BAD_REQUEST)


    def get(self, request,slug):
        if slug == "Song":
            song = Song.objects.all()
            data = SongSerializer(song, many=True).data
            return Response(data)
        elif slug == "Podcast":
            podcast = Podcast.objects.all()
            data = PodcastSerializer(podcast, many=True).data
            return Response(data)
        elif slug == "Audiobook":
            audiobook = Audiobook.objects.all()
            data = AudiobookSerializer(audiobook, many=True).data
            return Response(data)
        else:
            return Response({
                "errors": "Invalid  audioFileType"
            }, status.HTTP_400_BAD_REQUEST)


    
class AudioDetail(APIView):
    def get(self, request,slug, pk):
        if slug == "Song":
            try:
                song = Song.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Song with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
            data = SongSerializer(song).data
            return Response(data)
        elif slug == "Podcast":
            try:
                podcast = Podcast.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Podcast with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)

                data = PodcastSerializer(podcast).data
                return Response(data)
        elif slug == "Audiobook":
            try:
                audiobook = Audiobook.objects.get(pk =pk)
            except ObjectDoesNotExist:
                return Response({
                    "errors": "Audiobook with that id does not exists"
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
                data = AudiobookSerializer(audiobook).data
                return Response(data)
        else:
           return Response({
                "errors": "Invalid audioFileType. audioFileType can either be Song,Podcast or Audiobook "
            }, status.HTTP_400_BAD_REQUEST)