from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    '''Exibe a lista de tarefas'''
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('task_list')
            
    context = {'tasks': tasks, 'form':form}
    return render(request, 'tasks/task_list.html', context)

def delete_task(request, task_id):
    '''Deleta uma tarefa'''
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def update_task(request, task_id):
    '''Atualiza uma tarefa'''
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

def complete_task(request, task_id):
    '''Marca uma tarefa como completa'''
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
