from django.db import models

# Create your models here.
class Task(models.Model):
	title = models.CharField('Название', max_length=66)
	task_text = models.TextField('Описание')

	def __str__(self):
		return self.title

