from django.shortcuts import render , redirect
from django.template import loader
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from datetime import datetime
from datetime import datetime, timedelta
# from django_excel import make_response
import pandas as pd
import os


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
                    todo = toDoLists.objects.filter(username = uname , date = datetime.today().date())
                    total = todo.count()
                    remain = toDoLists.objects.filter(username = uname , date = datetime.today().date() , status = False).count()
                    comp = total - remain
                    context = {
                        'todo' : todo,
                        'total' : total,
                        'remain' : remain ,
                        'comp' : comp,
                        'name' : uname
                    }
                    print("total " , total , "remain" , remain ,'comp' , comp )
                    load = loader.get_template('todo.html')
                    return HttpResponse(load.render(context,request))
                else:
                    return redirect('/')
            else:
                return redirect('/')
        logs = log.objects.get(id = 1)
        todo = toDoLists.objects.filter(username = logs.username , date = datetime.today().date())
        total = todo.count()
        remain = toDoLists.objects.filter(username = logs.username , date = datetime.today().date() , status = False).count()
        comp = total - remain
        context = {
            'todo' : todo,
            'total' : total,
            'remain' : remain ,
            'comp' : comp ,
            'name' : logs.username,
        }  
        print("total " , total , "remain" , remain ,'comp' , comp )
        load = loader.get_template('todo.html')
        return HttpResponse(load.render(context,request))


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

def done(request , id):
    val = toDoLists.objects.get(id = id)
    val.status = True
    val.save()
    return redirect('login')

def undo(request , id):
    val = toDoLists.objects.get(id = id)
    val.status = False
    val.save()
    return redirect('login')

def logout(request):
    logs = log.objects.get(id = 1)
    logs.active = False
    logs.username = "nouser"
    logs.save()
    return redirect('/')

def past(request):
    logs = log.objects.get(id = 1)
    todo = toDoLists.objects.filter(username = logs.username )
    total = todo.count()
    remain = toDoLists.objects.filter(username = logs.username , status = False).count()
    comp = total - remain
    end_date = datetime.now().date() - timedelta(days=1)
    start_date = end_date - timedelta(days=7)
    todos = toDoLists.objects.filter(username = logs.username , date__range=(start_date, end_date))

    context = {
        'todo' : todos,
        'total' : total,
        'remain' : remain ,
        'comp' : comp ,
        'name' : logs.username,
    } 
    load = loader.get_template('past.html')
    return HttpResponse(load.render(context , request))

def goback(request):
    return redirect('login')

# def excel(request):
#     todo = toDoLists.objects.filter(username = "saran" )
#     data = list(todo.values())
#     df = pd.DataFrame(data)
#     df = df.drop(columns=['id','username'])
#     excel_file_path = 'file.xlsx'
#     df.to_excel(excel_file_path, index=False)
#     return HttpResponse(f'DataFrame has been saved to {excel_file_path}') 

def download_file(request):
    logs = log.objects.get(id = 1)
    todo = toDoLists.objects.filter(username = logs.username )
    data = list(todo.values())
    df = pd.DataFrame(data)
    
    df = df.drop(columns=['id','username'])
    df['status']=df['status'].replace(True,"Completed")
    df['status']=df['status'].replace(False,"Pending")
    excel_file_path = 'complete_todolist.xlsx'
    df.to_excel(excel_file_path, index=False)
    file_path = excel_file_path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        return HttpResponse("File not found", status=404)
def times(request):
    return HttpResponse(f'date is {datetime.now()},and time is {datetime.now()}')
    

