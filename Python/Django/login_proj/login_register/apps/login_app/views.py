########## APP LEVEL views ###########

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def root(request):
    return redirect("/login")

def index(request):
    return render(request, "login_app/index.html")



