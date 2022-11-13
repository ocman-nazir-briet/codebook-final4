from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import *
from .forms import *  
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        messages.warning(request,'you are already logged')
        return redirect('home')

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid Username')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'base/login.html', {'page':page})
            

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid Details........')
    return render(request, 'base/login.html', {'form':form})

# @login_required(login_url='/login')
def index(request):
    topic = Topic.objects.all()
    user = User.objects.all()
    q = request.GET.get('q') if request.GET.get('q')  != None else ''
    room = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    room_count=room.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    context = {'room':room, 'topic':topic, 'room_count':room_count,'room_messages':room_messages, 'user':user}

    return render(request, 'base/home.html', context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm
    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.host=request.user
            room.save() 
            return redirect('home')
    return render(request, 'base/createRoom.html', {'form':form})

def userProfile(request, pk):
    user=User.objects.get(id=pk)
    room = user.room_set.all()
    room_messages = user.message_set.all()
    topic = Topic.objects.all()
    context={'user':user, 'room':room, 'room_messages':room_messages, 'topic':topic}
    return render(request, 'base/userProfile.html', context)

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed to edit others Room')
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/update_room.html', {'form':form})

@login_required(login_url='/login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed to edit others Room')
    if request.method=='POST':
        room.delete()
        return redirect('/')
    return render(request, 'base/delete.html', {'obj':room})

@login_required(login_url='/login')
def detail(request, pk):
    obj = Room.objects.get(id=pk)
    room_message = obj.message_set.all().order_by('-created')
    participants = obj.participants.all()
    p_count = participants.count()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room = obj,
            body = request.POST.get('body')
        )
        obj.participants.add(request.user)
        return redirect('detail', pk=obj.id)

    return render(request, 'base/detail.html', {'obj':obj, 'room_message':room_message, 'participants':participants, 'p_count':p_count})

@login_required(login_url='/login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed to edit others message')
    if request.method=='POST':
        message.delete()
        return redirect('/')
    return render(request, 'base/delete.html', {'obj':message})
