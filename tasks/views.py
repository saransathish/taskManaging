from django.shortcuts import render , redirect
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
# Create your views here.
def index(request):
    load = loader.get_template('index.html')
    return HttpResponse(load.render({},request))
def login(request):
        if request.method == 'POST':
            uname = request.POST['uname']
            password = request.POST['password']
            val = users.objects.filter(username = uname)
            if val:
                data = users.objects.get(username = uname)
                if data.password == password:
                    logs = log.objects.get(id = 1)
                    logs.username = uname
                    logs.active = True 
                    logs.save()

                    
                    load = loader.get_template('todo.html')
                    return HttpResponse(load.render({},request))
                else:
                    return redirect('/')
            else:
                return redirect('/')
            
        load = loader.get_template('todo.html')
        return HttpResponse(load.render({},request))
def signup(request):
    load = loader.get_template('signin.html')
    return HttpResponse(load.render({},request))
def back(request):
    return redirect('/')
def createuser(request):
    username = request.POST['username']
    fullname = request.POST['fullname']
    email = request.POST['email']
    password = request.POST['password']
    if password and email and username and fullname:
        load = users(username = username,fullname = fullname,email = email,password = password)
        load.save()
        return redirect('/')  
    else:
        return redirect('signup')
def createtodo(request):
    job = request.POST['job']
    type = request.POST['type']
    logs = log.objects.get(id = 1)
    load = toDoLists(username = logs.username , job = job , status = False , job_type = type) 
    load.save()
    return redirect('login')