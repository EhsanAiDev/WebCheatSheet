from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.messages import success , error
from django.contrib.auth.models import User

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
