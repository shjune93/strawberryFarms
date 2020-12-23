from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import User
# Create your views here.
def users_login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username,password=password)
        if user is not None:
            print("인증성공")
            login(request,user)
        else:
            print("인증실패")
    return render(request,"users/login.html")


def users_logout(request):
    logout(request)
    return redirect("users:login")


def users_signup(request):
    if request.method=="POST":
        print(request.POST)
        username=request.POST["username"]
        password=request.POST["password"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]

        user=User.objects.create_user(username,email,password)
        user.last_nam=lastname
        user.save()
        return redirect("users:login")

    return render(request,"users/signup.html")