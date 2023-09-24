# cloud_server_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

def file_upload_to(instance, filename):
    return f'{instance.device.user.username}/{instance.device.name}/{filename}'

class File(models.Model):
    name = models.CharField(max_length=255)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_upload_to)