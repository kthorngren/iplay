from models import Todo
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
#from todo.app.forms import *
from django.template import RequestContext


def index(request): #Define our function, accept a request
 
    items = Todo.objects.all() #ORM queries the database for all of the to-do entries.
 
    return render(request, 'index.html', {'items': items}) #Responds with passing the object items (contains info from the DB) to the template index.html

def add_todo(request):
    if request.method=='POST':
        todo_obj=Todo(description=request.POST.get('job'))
        todo_obj.save()
        return HttpResponseRedirect('/todo')
    else:
        data=RequestContext(request)
        return render(request, 'add_todo.html', data.pop())

def edit_todo(request):
    if request.method=='POST':
        todo_obj=Todo.objects.filter(id=request.POST.get('id')).update(description=request.POST.get('job'))
        return HttpResponseRedirect('/todo')
    else:
        id = request.GET.get('id')
        todo_obj=Todo.objects.filter(id=id)
        data=RequestContext(request)
        return render(request, 'edit_todo.html', {'todo': todo_obj[0]})

def delete_todo(request):
    id = request.GET.get('id')
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect('/todo')

