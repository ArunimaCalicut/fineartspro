from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from artsapp.forms import Loginform


def home(request):
    return render(request,'home.html')

def login_view(request):
    form =Loginform()
    if request.method =='POST':
        form=Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username ,password=password)
            if user is not None:
                login(request,user)
                if user.is_staff:
                  return redirect('admin_home')
                if user.is_teacher:
                    return redirect('teacher_home')
                if user.is_student:
                    return redirect('student_home')
                else:
                    messages.info(request,"Invalid Credentials")
    return render(request,'login.html', {'form':form})

def admin_home(request):
    return render(request,'admin_home.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')







