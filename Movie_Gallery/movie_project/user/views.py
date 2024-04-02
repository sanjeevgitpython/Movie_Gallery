from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        emailid = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=emailid).exists():
                messages.info(request,'email address already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=emailid,password=password)
                user.save()
                print('user created')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('login')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def view_profile(request):
    return render(request, 'view_profile.html', {'user': request.user})

def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'edit_user.html', {'form': form})
