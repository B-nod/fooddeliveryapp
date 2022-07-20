from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.models import *

from .forms import LoginForm, SignUpForm

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account Created')
            return redirect('/register')
        else:
            messages.add_message(request,messages.ERROR, 'Please provie correct details')
            return render(request, 'users/register.html',{'form':form})
    context={
        'form':SignUpForm
    }
    return render(request, 'users/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, email=data['email'], password=data['password'])
            
            if user is  not None:
                login(request,user)
                if user.is_staff:
                    return redirect('/admins/dashboard')
                else:
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR, 'Please provide correct credentails ')
                return render(request,'users/login.html',{
                    'forms':form
                })

    form = LoginForm
    context = {
        'form': form
    }
    return render(request,'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/login')

def homepage(request):
    restaurents = Restaurent.objects.all().order_by('-id')[:8]
    context = {
        'restaurents': restaurents,
    }
    return render(request, 'users/index.html',context)