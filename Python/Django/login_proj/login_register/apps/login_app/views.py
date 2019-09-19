########## APP LEVEL views ###########

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User


def root(request):
    return redirect("/index")

def index(request):
    print(User.objects.last().first_name)
    return render(request, "login_app/index.html")

def success(request):
    return render(request, "login_app/success.html")


def reg(request):
    print("we run and register!")
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/index") 
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            birthday = request.POST['birthday']
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, birthday=birthday, password=password)
            messages.success(request, "User successfully registered")
        return redirect("/success")

def login(request):
    errors={}
    print("login user works!"+"*"*80)
    if request.method == "POST":
        other_user = User.objects.filter(email = request.POST['email'])
        try:
            this_user = other_user[0]
            if request.POST['password'] == this_user.password:
                return redirect("/success")
            errors["password_error"] = "You forgot your password"
        except:
            errors['email_error']= "No user exists here, go ahead and register"
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
    return redirect("/")
            


