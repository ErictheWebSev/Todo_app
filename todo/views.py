from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm


def todo_view(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			task = Task.objects.create(title=title)
			return redirect('todo')
	else:
		form = TaskForm()
	
	tasks = Task.objects.all()
	context = {
		'form': form,
		'tasks': tasks
	}
	return render(request, 'task-list.html', context)


def task_delete(request, id):
	task = Task.objects.get(id=id)
	if request.method == 'POST':
		task.delete()
		return redirect('todo')
	

def task_completed(request, id):
	task = Task.objects.get(id=id)
	task.completed = not task.completed
	task.save()
	return redirect('todo')


def task_update(request, id):
	task = get_object_or_404(Task, id=id)
	if request.method == 'POST':
		updated = request.POST.get('updated_title')
		task.title = updated
		task.save()
		return redirect('todo')
	