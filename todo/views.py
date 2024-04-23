from django.shortcuts import render, redirect
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

def remove(request, id):
    item = ToDo.objects.get(id=id)
    item.delete()
    messages.info(request, "Item deleted")
    return redirect('todo')


