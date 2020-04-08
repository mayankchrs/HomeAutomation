from django.urls import include,path
from . import views

urlpatterns = [
  path('deviceList/', views.getdevice),
  path('add_device/', views.add_device),
  path('update_device/', views.update_device),
  path('delete_device/', views.delete_device)
]