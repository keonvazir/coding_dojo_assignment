######### APP LEVEL views.py

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("THIS WORKSSSS!")
