########## APP LEVEL views ###########
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, User

def index(request):
    return render(request, "login_app/index.html")

def success(request):
    if "first_name" in request.session:
        context = {
            "books": Book.objects.all(),
        }
        return render(request, "login_app/success.html", context)
    return redirect("/")

def one_book(request, book_id):
    book = Book.objects.get(id = book_id)
    this_book_fans = book.fans.all()
    context = {
        "book":book,
        "this_book_fans": this_book_fans,
    }
    return render(request, "login_app/book.html", context)

def add_book(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        title = request.POST["book_title"]
        description = request.POST["book_description"]
        new_book = Book.objects.create(title=title, description=description)
        new_book.fans.add(User.objects.get(id=request.session['id']))
        return redirect("/success")

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
                return redirect("/success")
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
    return redirect("/success")

def logout(request):
    request.session.clear()
    return redirect("/")
            


