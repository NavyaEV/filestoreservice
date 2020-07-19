from django.test import TestCase
from filestore.models import File
from filestore.serializers import FileSerializer
import tarfile
import os
from filestore.views import FileList
import mock
#import JSONParser

class FileTestCase(TestCase):
    def test_checkTarFileExists(self):
        self.assertEqual(False, os.path.exists('%s/sample.tar'%os.getcwd()))

    def test_model(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'sample.tar'
        file_model = File(file=file_mock)
        self.assertEqual(file_model.file.name, file_mock.name)

    def test_model_serializer(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'sample.tar'
        file_mock.file = 'sample.tar'
        file_model = File(file=file_mock.file, name=file_mock.name)
        file_serializer = FileSerializer(file_model)
        self.assertEqual('/media/sample.tar', file_serializer.data['file'])
        self.assertEqual('sample.tar', file_serializer.data['name'])

