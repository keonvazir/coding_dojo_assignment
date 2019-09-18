########## APP LEVEL views ###########

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def root(request):
    return redirect("/")

def index(request):
    return render(request, "login_app/index.html")



