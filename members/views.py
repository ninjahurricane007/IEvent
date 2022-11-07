from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from members.models import Profile
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user);
            return redirect('/fests')
        else:
            messages.success(request,("Invalid credentials"))
            return redirect('login')
    return render(request,'Login/login.html')

def user_logout(request):
    logout(request)
    messages.success(request,("You Were Logged Out!"))
    return redirect('/')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        hashed_password = make_password(password)
        email = request.POST['email']
        try:
            if User.objects.filter(email=email).exists():
                messages.success(request, ('Already have an account with same email id'))
                return redirect('/auth/signup')
            else:
                user = User(username=username,password=hashed_password,email=email)
                user.save()
                Profile.objects.create(user=user)
                user = authenticate(request, username=username, password=password)
                login(request,user);
                return redirect('/fests')
        except :
            messages.success(request, ('Already have an account with same email id'))
            return redirect('/auth/signup')
    return render(request,'Signup/signup.html')