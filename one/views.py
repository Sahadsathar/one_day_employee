from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def home (request):
    return render(request, 'home.html')

def newsfeed (request):
    return render(request, 'feed.html')

def signup (request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password-2']
        if password == password2:
            if User.objects.filter(email=email).exist():
                messages.info(request, 'Email already taken')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('/signup')
            else:
                user= User.objects.create_user(username=username, email=email,password=password)
                user.save()
    else:
        messages.info(request, 'password is not correct')
        return render(request, 'signup.html')