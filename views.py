from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')  # Redirect to the signup page

        # Check if the username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')  # Redirect to the signup page

        # Create a new user
        user = User.objects.create_user(username=uname, email=email, password=pass1)
        user.save()
        messages.success(request, 'User created successfully!')
        return redirect('homepage')  # Redirect to the homepage or another page

    return render(request, 'signup.html')

def HomePage(request):
    return render(request, 'homepage.html')




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('homepage')  # Redirect to a different page after login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')




