from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .models import User
# Create your views here.
def users_login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        #로그인이 필요한 화면에서 왔을때
        beforePage=request.GET.get('next',"post/post_list")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            #이전 화면으로 다시 보내준다
            return redirect(beforePage)
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