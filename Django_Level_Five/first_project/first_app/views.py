from django.shortcuts import render
#from . import forms
from first_app.forms import UserForm,UserInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def base(request):
    return render(request,'first_app/base.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        info_form = UserInfoForm(request.POST,request.FILES)

        if user_form.is_valid() and info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            info = info_form.save(commit=False)
            info.user = user

            if 'pro_pics' in request.FILES:
                info.pro_pics = request.FILES['pro_pics']

            info.save()
            registered = True
        else:
            print(user_form.errors,info_form.errors)
    else:
        user_form = UserForm()
        info_form = UserInfoForm()

    return render(request,'first_app/registration.html',
                           {'user_form':user_form,
                            'info_form':info_form,
                             'registered':registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details!")
    else:
        return render(request,'first_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")
