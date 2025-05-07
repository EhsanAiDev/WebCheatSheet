from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.messages import success , error
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def LoginPage(r):
    if not r.user.is_authenticated:
        if r.method == "POST" and "login" in r.POST:
            username = r.POST.get("username")
            password = r.POST.get("password")

            try:
                User.objects.get(username=username)
            except:
                error(r , "the user account is not exist")
            else:
                auth = authenticate(r,username=username,password=password)

                if auth is not None :
                    login(r , auth)
                    success(r , "loggined successfuly")
                    return redirect("home")
                else:
                    error(r , "the password is not correct")
    else:
        error(r , "you'r already loggined")
        return redirect("home")
    return render(r ,"UserSystem/login.html")

def RegisterPage(r):
    if not r.user.is_authenticated:
        if r.method == "POST" and 'singup' in r.POST:
            form = UserCreationForm(r.POST)
            if form.is_valid():
                user = form.save()
                login(r , user=user)
                return redirect('home')
            else:
                errors = form.errors.items()
                for i,error_text in errors:
                    error(r , error_text)
    else:
        error(r , "you'r already loggined")
        return redirect('home')
    return render(r ,"UserSystem/register.html")

def LogOutPage(r):
    logout(r)
    success(r , "Logouted successfuly")
    return redirect("home")

def ChangePasswordPage(r):
    if r.user.is_authenticated:
        if r.method == "POST":
            form = PasswordChangeForm(r.user, r.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(r, user)
                success(r,"the password changed successfully")
                return redirect('profile')              
            else:
                errors = form.errors
                for key,value in errors.items():
                    error(r,value.as_text().replace("* " , ""))
        return render(r,"UserSystem/change_password.html")
    else:
        error(r,"you are not authenticated")
        return redirect("home")

def ProfilePage(r,pk):
    user = get_object_or_404(User, username=pk)
    
    return render(r , "UserSystem/profile.html", context={"user":user})
