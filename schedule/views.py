from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import scheduleForm
from .forms1 import CreateUser
from .models import schedule
from django.contrib import messages
# Create your views here.

def index(request):
    form = schedule.objects.all()
    context = {'form':form}
    return render(request, 'index.html', context)


def scheduled(request):
    if request.method == 'POST':
        form = scheduleForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('/')
        else:
            return render(request, 'schedule.html', {'form':form})
    else:
        form = scheduleForm()
        return render(request, 'schedule.html', {'form':form})

def register(request):
    if request.method =='POST':  
        form = CreateUser(request.POST)
        if form.is_valid():     
            post = form.save()
            post.save()  
            # return HttpResponse('login')
            return redirect('login')
        # else:
        #     return render(request, "register.html", {'form':form})  
    else:
        form = CreateUser()   
        return render(request, 'register.html', {'form':form})

def loginPage(request):
    form = CreateUser()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {'form':form}
    return render(request, 'login.html', context)

def delete(request, pk):
    obj = schedule.objects.get(id=pk)
    obj.delete()
    return redirect('/')
