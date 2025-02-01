from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    title = ' Django!!'
    return render(request, 'index.html', {'title' : title})

def about(request):
    return render(request, 'about.html')

def tasks(request):
    task =  Task.objects.get(id=1)
    return render(request, 'task.html', {'task': task})

def projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects.html', {'projects' : projects})
