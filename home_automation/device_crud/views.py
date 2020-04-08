from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .serializers import RoomSerializer, DeviceSerializer
from .models import Room, Device
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import json


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def getdevice(request):
    user = request.user.id
    devices = Device.objects.filter(added_by=user)
    serializer = DeviceSerializer(Device, many=True)
    return JsonResponse({'devices': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_device(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        room = Room.objects.get(id=payload["room"])
        device = Device.create(
            name=payload["name"],
            room=room,
            added_by=user
        )
        serialize = DeviceSerializer(device)
        return JsonResponse({'device': serialize.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went Wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_device(request, device_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        device_item = Device.objects.filter(added_by=user, id=device_id)
        device_item.update(**payload)
        device = Device.objects.get(id=device_id)
        serializer = DeviceSerializer(device)
        return JsonResponse({'device': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_device(request, device_id):
    user = request.user.id
    try:
        book = Device.objects.get(added_by=user, id=device_id)
        book.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)