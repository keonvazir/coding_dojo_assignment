############ APP LEVEL ###############

from django.shortcuts import render, HttpResponse, redirect
from .models import Roster, User

def index(request):
    context = {
        "rosters": Roster.objects.all(),
    }
    return render(request, "roster_user_app/index.html", context)

def add_roster(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        title = request.POST['roster_title']
        description = request.POST['roster_description']
        Roster.objects.create(title=title, description=description)
        return redirect("/")

