from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList
from .forms import TodoForm

def index(request):
	todo = TodoList.objects.all()
	return render(request, 'todo/index.html', {'todo': todo})

def TodoNew(request):
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('TodoDetail', pk=todo.pk)
	else:
		form = TodoForm()
	return render(request, 'todo/TodoEdit.html', {'form': form})

def TodoDetail(request, pk):
	todo = get_object_or_404(TodoList, pk=pk)
	return render(request, 'todo/TodoDetail.html', {'todo': todo})


def TodoEdit(request, pk):
	todo = get_object_or_404(TodoList, pk=pk)
	if request.method == "POST":
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('TodoDetail', pk=todo.pk)
	else:
		form = TodoForm(instance=todo)
		return render(request, 'todo/TodoEdit.html', {'form': form})