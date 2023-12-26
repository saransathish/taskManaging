from django.shortcuts import render , redirect
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
# Create your views here.
def index(request):
    load = loader.get_template('index.html')
    return HttpResponse(load.render({},request))
def login(request):
        uname = request.POST['uname']
        password = request.POST['password']
        val = users.objects.filter(username = uname)
        if val:
            data = users.objects.get(username = uname)
            if data.password == password:
                load = loader.get_template('todo.html')
                return HttpResponse(load.render({},request))
            else:
                return redirect('/')
        else:
            return redirect('/')
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

