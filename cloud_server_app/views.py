#cloud_server_app/views.py
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from .models import File, Device
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in, redirect, or whatever you like here
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

class FileListView(generic.ListView):
    model = File
    template_name = 'cloud_server_app/file_list.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        device = get_object_or_404(Device, user=user, id=self.kwargs['device_id'])
        directory_path = os.path.join(settings.MEDIA_ROOT, user.username, device.name)
        
        if os.path.exists(directory_path):
            file_names = os.listdir(directory_path)
        else:
            file_names = []
            
        return file_names

def download_file(request, device_id, file_name):
    device = Device.objects.get(id=device_id)
    file_path = os.path.join(settings.MEDIA_ROOT, device.user.username, device.name, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    else:
        # Handle the case where the file does not exist
        # You can return an error page or redirect to another view
        return HttpResponse("File not found", status=404)
    
class DeviceListView(generic.ListView):
    model = Device
    template_name = 'cloud_server_app/device_list.html'
def add_device(request):
    if request.method == "POST":
        device_name = request.POST.get('device_name')
        if device_name:
            Device.objects.create(name=device_name)
        return redirect('device-list')  # Redirect back to the device list page

