from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):

	class Meta:
		model = Task
		fields = ["title", "task_text"]
		widgets = {
		"title": TextInput(attrs={
			"class": 'form-control',
			"placeholder": 'Введите название'
			}),
		"task_text": Textarea(attrs={
			"class": 'form-control',
			"placeholder": 'Введите описание'
			}),
		}