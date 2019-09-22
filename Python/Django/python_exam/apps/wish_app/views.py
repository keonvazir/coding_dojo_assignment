########### APP LEVEL ##############

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Wish

def index(request):
    return render(request, "wish_app/index.html")

def login(request):
    errors={}
    if request.method == "POST":
        other_user = User.objects.filter(email = request.POST['email'])
        try:
            this_user = other_user[0]
            if request.POST['password'] == this_user.password:
                request.session['first_name'] = this_user.first_name
                request.session['id'] = this_user.id
                request.session['last_name'] = this_user.last_name
                return redirect("/wishes")
            errors["password_error"] = "You forgot your password"
        except:
            errors['email_error']= "No user exists here, go ahead and register"
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
    return redirect("/")

def reg(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/") 
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['confirm_password']
            new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
            messages.success(request, "User successfully registered")
            request.session['first_name']=new_user.first_name
            request.session['last_name']=new_user.last_name
            request.session['id']=new_user.id
    return redirect("/wishes")

def dashboard(request):
    if "first_name" in request.session:
        context = {
            "all": [wish for wish in Wish.objects.filter(wished_for_by=request.session['id']) if wish.granted==False],
            "granted_wishes": Wish.objects.filter(granted=True),
        }
        return render(request, "wish_app/dashboard.html", context)
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")
    
def new_wish(request):
    if "first_name" in request.session:
        context = {
            "all_wishes": Wish.objects.all(),
            "users": User.objects.all(),
        }
        return render(request, "wish_app/make_wish.html", context)
    return redirect("/wishes")

def add_wish(request):
    if request.method == "GET":
        return redirect("/wishes")
    if request.method == "POST":
        errors = Wish.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            # wish = Wish.objects.all()
            return redirect("/wishes/new")
        else:
            item = request.POST['new_item']
            description = request.POST['new_description']
            wish = Wish.objects.create(item=item, description=description)
        return redirect("/wishes")

def edit_page(request, wish_id):
    if "first_name" in request.session:
        wish_id = Wish.objects.get(id=wish_id)
        all_wish = Wish.objects.all()
        context = {
            "wish": wish_id,
            "users": User.objects.all(),
            "all_wishes": Wish.objects.all(),
        }
    return render(request, "wish_app/edit.html", context)

def edit_wish(request, wish_id):
    if request.method == "GET":
        return redirect("/shows")
    if request.method == "POST":
        errors = Wish.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/wishes"+"/edit/"+str(wish_id))
        else:
            this_wish = Wish.objects.get(id=wish_id)
            this_wish.item = request.POST['new_item']
            this_wish.description = request.POST['new_description']
            this_wish.save()
            return redirect("/wishes")

def remove(request, wish_id):
    remove_wish = Wish.objects.get(id=wish_id)
    remove_wish.delete()
    return redirect("/wishes")


def granted(request, wish_id):
        this_wish = Wish.objects.get(id=wish_id)
        this_wish.granted = True
        this_wish.save()
        return redirect("/wishes")

def like(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    #wish_user = wish.user.all()
    session_user = User.objects.get(id=request.session['id'])
    if session_user not in wish.user.all():
        wish.user.add(session_user)
        return redirect("/wishes")
    wish.user.remove(session_user)
    return redirect("/wishes")