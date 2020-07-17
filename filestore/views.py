from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import File
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from django.conf import settings
import os
from django.http import HttpResponse
from rest_framework.views import APIView

class FileList(APIView):
    http_method_names = ['post', 'get', 'delete']
    def get(self, request, format=None):
        filesList = File.objects.all()
        serializer = FileSerializer(filesList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.validated_data['file'])
            serializer.validated_data['name'] = serializer.validated_data['file']
            filesList = File.objects.filter(name=serializer.validated_data['name'])
            if filesList.count() > 0:
                returnMessage = {}
                returnMessage['Message'] = 'File already exists'
                return Response(returnMessage, status=status.HTTP_409_CONFLICT)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        file = File.objects.filter(name=request.data.get('name'))
        if file.count() == 0:
            returnMessage = {}
            returnMessage['Message'] = 'File does not exist to delete or already deleted'
            return Response(returnMessage, status=status.HTTP_404_NOT_FOUND)
        file.delete()
        return Response({'Message':'Successfully deleted'}, status=status.HTTP_204_NO_CONTENT)

class FileDownload(generics.CreateAPIView):
    http_method_names = ['get']    
    def get(self, request, format=None):
        fileAbsPath = '%s/%s/%s'%(settings.MEDIA_ROOT, settings.MEDIA_SUB_DIR_NAME, request.data['file'])
        print(fileAbsPath)
        if os.path.exists(fileAbsPath):
            with open(fileAbsPath, 'rb') as f:
                file_data = f.read()
            response = HttpResponse(file_data, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="%s"'%request.data['file']
            return response
        returnMessage = {}
        returnMessage['Message'] = 'File does not exist'
        return Response(returnMessage, status=status.HTTP_400_BAD_REQUEST)
