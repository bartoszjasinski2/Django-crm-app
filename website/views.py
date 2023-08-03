from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been loggen in")
			return redirect('home')
		else:
			messages.success(request, "There was an Error Logging in, please tgry again")
			return redirect('home')
	else:
		return render(request, 'home.html', {})




def logout_user(request):
	print("000")
	logout(request)
	print("111")
	messages.success(request, "You have beem Logged Out")
	print("222")
	return redirect('home')

def register_user(request):
	return render(request, 'register.html', {})

