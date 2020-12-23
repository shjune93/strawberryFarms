from django.urls import path
from .import views

app_name="users"

urlpatterns = [
    path("login",views.users_login,name="login"),
    path("logout",views.users_logout,name="logout"),
    path("signup",views.users_signup,name="signup")
]