from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TimeModel
import time


# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.create_user(username, '', password)
                user = authenticate(request, username=username, password=password)
                login(request, user)
                object = TimeModel.objects.create(
                    user_id = user.id,
                    departure_time = 0,
                    return_time = 0,
                    out_time = 0
                )
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'error':'このユーザーは既に登録されています'})
    return render(request, 'signup.html')

def loginfunc(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			return render(request, 'login.html', {})
	return render(request, 'login.html', {})

def logoutfunc(request):
	logout(request)
	return redirect('login')

@login_required
def homefunc(request):
    return render(request, 'home.html')

@login_required
def gofunc(request):
    user = request.user
    object = TimeModel.objects.get(user_id=user.id)
    object.departure_time = int(time.time())
    object.save()
    return render(request, 'go.html')

@login_required
def backfunc(request):
    user = request.user
    object = TimeModel.objects.get(user_id=user.id)
    object.return_time = int(time.time())
    object.out_time = object.return_time - object.departure_time
    object.save()
    return render(request, 'back.html', {'object':object})
    
