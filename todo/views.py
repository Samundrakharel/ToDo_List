from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import ToDo
from .forms import ToDoForm
# Create your views here.

def index(request):
    to_do_list = ToDo.objects.order_by('-date')
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = ToDoForm
    context = {
        'forms' : form,
        'list' : to_do_list,
        'title' : 'TODO LIST'
    }
    return render(request, 'todo/index.html', context)

def edit(request, id):
    item = get_object_or_404(ToDo, id=id)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = ToDoForm(instance=item)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'todo/index.html', {'form': form, 'item': item})
    else:
        return render(request, 'todo/index.html', {'form': form, 'item': item})

def remove(request, id):
    item = ToDo.objects.get(id=id)
    item.delete()
    messages.info(request, "Item is deleted")
    return redirect('todo')


