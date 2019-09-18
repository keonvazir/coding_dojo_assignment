########## APP LEVEL views ###########

from django.shortcuts import render

def index(request):
    return render(request, "login_app/index.html")



