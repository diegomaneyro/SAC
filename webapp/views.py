from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Project, Task
from django.shortcuts import get_object_or_404, redirect
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = 'Django!!'
    return render(request, 'index.html', {'title' : title})

def about(request):
    return render(request, 'about.html')

def tasks(request):
    tasks =  Task.objects.all().order_by('id')
    return render(request, 'tasks.html', {'tasks': tasks})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects' : projects})

def create_task(request):
    if request.method == 'GET': 
        return render(request, 'create_task.html',{
            'form': CreateNewTask()
        })    
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/tasks/')
        