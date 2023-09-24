#cloud_server_app/urls.py
from django.urls import path
from .views import FileListView, DeviceListView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('devices/', DeviceListView.as_view(), name='device-list'),
    path('devices/<int:device_id>/download/<str:file_name>/', views.download_file, name='download_file'),
    path('download/<str:file_name>/', views.download_file, name='download_file'),   
    path('add_device/', views.add_device, name='add-device'),
    path('<str:username>/devices/<int:device_id>/files/', FileListView.as_view(), name='file-list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]