from django.shortcuts import render
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
                    departure_time = time.time() * 10**7,
                    return_time = time.time() * 10**7,
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

def homefunc(request):
    return render(request, 'home.html')

def gofunc(request):
    user = request.user
    object = TimeModel.objects.get(user_id=user.id)
    object.departure_time = time.time() * 10**7
    object.save()
    return render(request, 'go.html')

def backfunc(request):
    user = request.user
    object = TimeModel.objects.get(user_id=user.id)
    object.return_time = time.time() * 10**7
    object.out_time = object.return_time - object.departure_time
    object.save()
    return render(request, 'back.html', {'object':object})
    
