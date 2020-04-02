from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method== 'POST':
        if request.POST['password']==request.POST['confirm-password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already taken!!!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match!!!'})
    else:
        return render(request, 'accounts/signup.html')
    
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    # TODO: need to route to homepage
    # Need to add logout
    return render(request, 'accounts/logout.html')
