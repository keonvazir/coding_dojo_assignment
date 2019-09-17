########## APPS LEVEL views.py file ##############

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all the blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, my_val):
    return HttpResponse("placeholder to display blog number: {my_val}")

def edit(request, my_val):
    return HttpResponse("placeholder to edit the blog: {my_val}")

def delete(request):
    return redirect("/")




# Create your views here.
