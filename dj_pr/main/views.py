from django.shortcuts import render
from .models import Task

# Create your views here
def index(request):
	tasks = Task.objects.all()
	return render(request, 'main/index.html', {'tasks': tasks})

def about(request):
	return render(request, 'main/about.html')
	

