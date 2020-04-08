from django.urls import include,path
from . import views

urlpatterns = [
  path('deviceList/', views.getdevice),
  path('add_device/', views.add_device)
]