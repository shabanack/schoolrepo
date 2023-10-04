from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cfmpassword = request.POST.get('cfmpassword')
        if password==cfmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)

                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
    return render(request, "register.html")

def formpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        user = auth.authenticate(username=username,email=email)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            #messages.info(request, "invalid credentials")
            return redirect('/')
    return render(request, "formpage.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
