from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here
def index(request):
	tasks = Task.objects.all()
	return render(request, 'main/index.html', {'tasks': tasks})

def about(request):
	return render(request, 'main/about.html')

def create(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Ошибка при заполнении формы'

	form = TaskForm()
	context = {
		'form': form
	}
	return render(request, 'main/create.html', context)
	

