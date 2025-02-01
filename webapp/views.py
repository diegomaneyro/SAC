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
    tasks =  Task.objects.all().order_by('id')
    return render(request, 'task.html', {'tasks': tasks})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects' : projects})
