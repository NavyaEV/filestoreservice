from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(max_length=None)
    class Meta():
        model = File
        fields = ['name', 'file', 'created']
