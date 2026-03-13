from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from user_auth.forms import UserForm, LoginForm

# Create your views here.
def register(request):

    if request.method == "POST":
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            username=request.POST['username'],
        )
        user.set_password(request.POST['password'])
        user.save()
        return redirect('login')

    return render(request, 'register.html')


def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_is_auth = authenticate(username=username, password=password)
        print(user_is_auth)
        if user_is_auth:
            login(request, user_is_auth)
            return redirect('flights')
        else:
            return render(request, 'login.html', {'incorrect':True})

    return render(request, 'login.html')


def profile(request):

    return render(request, 'profile.html')


def logout_(request):
    logout(request)
    return redirect('login')


def update_profile(request):
    user = request.user

    if request.method == 'POST':
        new_firstname=request.POST['first_name']
        new_lastname=request.POST['last_name']
        new_email=request.POST['email']
        new_username=request.POST['username']

        
        if User.objects.filter(username=new_username):
            return render(request, 'update_profile.html', {'notnew':True})
        else:
            user.first_name=new_firstname
            user.last_name=new_lastname
            user.email=new_email
            user.username=new_username
            user.save()
            return redirect('profile')
            
    return render(request, 'update_profile.html', {'user':user})
    

def reset_pass(request):
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        old_pass=request.POST['oldpassword']
        new_pass=request.POST['newpassword']
        
        if (old_pass==""):
            return render(request, 'reset_pass.html', {'empty':True})
        
        elif (old_pass!=new_pass):
            user.set_password(new_pass)
            user.save()
            # print(old_pass, new_pass)
            return redirect('login')
        
        else:
            return render(request, 'reset_pass.html', {'notnew':True})
    return render(request, 'reset_pass.html')