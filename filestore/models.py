from django.db import models
from django.conf import settings

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length = 50, null=True, blank=True)
    file = models.FileField(blank=False, null=False, upload_to='%s/'%settings.MEDIA_SUB_DIR_NAME, unique=True)
    created = models.DateTimeField(auto_now_add=True)

