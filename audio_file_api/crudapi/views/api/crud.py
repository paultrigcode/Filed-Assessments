from django.shortcuts import render
from crudapi.models import Song,Podcast,Audiobook
from crudapi.serializers import SongSerializer,PodcastSerializer,AudiobookSerializer
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.views import APIView





class ArticleView(APIView):
    def delete(self,request,pk,slug):
        print(slug)
        if slug == "Song":
            Song.objects.filter(id =pk).delete()
            return Response({
                "status": "success",
            })
        elif slug == "Podcast":
            Podcast.objects.filter(id =pk).delete()
            return Response({
                "status": "success",
            })
        elif slug == "Audiobook":
            Audiobook.objects.filter(id =pk).delete()
            return Response({
                "status": "success",
            })
        else:
             return Response({
                "status": "error",
            })

    def post(self, request):
        file_type = request.data["audioFileType"]
        if file_type == "Song":
            name = request.data["name"]
            duration = request.data['duration']
            song = Song.objects.create(name = name,duration_in_number_of_seconds = duration)
            return Response({
                "status": "success",
                "data": model_to_dict(song)
            })

        elif file_type == "Podcast":
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
            title = request.data["title"]
            author = request.data["author"]
            narrator = request.data["narrator"]
            duration = request.data['duration']
            audiobook = Audiobook.objects.create(title = titlr,duration_in_number_of_seconds = duration, author = author,narrator = narrator)
            return Response({
                "status": "success",
                "data": model_to_dict(audiobook)
            })

        else:
             return Response({
                "errors": "Invalid   audioFileType"
            }, status.HTTP_400_BAD_REQUEST)


    def put(self,request,slug,pk):
        if slug == "Song":
            print(request.data)
            name = request.data["name"]
            duration = request.data['duration']
            song = Song.objects.get(pk=pk)
            song.name = name
            song.duration =duration
            song.save()
            return Response({
                "status": "success",
                "data": model_to_dict(song)

            })

        elif slug == "Audiobook":
            print(request.data)
            title = request.data["title"]
            author = request.data["author"]
            narrator = request.data["narrator"]
            duration = request.data['duration']
            audiobook = Audiobook.objects.get(pk=pk)
            audiobook.title = title
            audiobook.author = author
            audiobook.narrator = narrator
            audiobook.duration = duration
            audiobook.save()
            return Response({
                "status": "success",
                "data": model_to_dict(podcast)

            })

        elif slug == "Podcast":
            print(request.data)
            name = request.data["name"]
            duration = request.data['duration']
            host = request.data['host']
            podcast = Podcast.objects.get(pk=pk)
            podcast.name = name
            podcast.duration =duration
            podcast.host = host
            podcast.save()
            return Response({
                "status": "success",
                "data": model_to_dict(podcast)

            })
        else:
            return Response({
                "status": "error",
            })

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
                "status": "error",
            })

    
class ArticleDetail(APIView):
    def get(self, request,slug, pk):
        if slug == "Song":
            song = Song.objects.get(pk =pk)
            if song.DoesNotExist():
                 return Response({
                    "status": "error",
                })            
            else:
                 
                data = SongSerializer(song).data
                return Response(data)
        elif slug == "Podcast":
            podcast = Podcast.objects.get(pk = pk)
            if song.DoesNotExist():
                 return Response({
                    "status": "error",
                })    
            else:
                data = PodcastSerializer(podcast).data
                return Response(data)
        elif slug == "Audiobook":
            audiobook = Audiobook.objects.get(pk = pk)
            if song.DoesNotExist():
                 return Response({
                    "status": "error",
                })    
            else:
                data = AudiobookSerializer(audiobook).data
                return Response(data)
        else:
             return Response({
                "status": "error",
            })






        






