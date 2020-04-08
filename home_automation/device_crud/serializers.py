from rest_framework import serializers
from .models import Room, Device


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'house_name', 'room_name', 'added_by', 'created_date']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'status', 'intensity', 'room', 'added_by', 'created_date']
