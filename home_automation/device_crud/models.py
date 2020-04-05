from django.db import models
from django.conf import settings
from django.utils import timezone

class Room(models.Model):
    house_name = models.CharField(max_length=30)
    room_name = models.CharField(max_length=30)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.room_name

class Device(models.Model):
    name = models.CharField(max_length=25)
    status = models.BooleanField(default=0)
    intensity = models.IntegerField(default=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# Create your models here.
