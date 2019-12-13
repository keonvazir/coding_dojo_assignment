############ APP LEVEL ###############

from django.shortcuts import render, HttpResponse, redirect
from .models import Roster, User

def index(request):
    context = {
        "rosters": Roster.objects.all(),
    }
    return render(request, "your_app_name_here/index.html", context)

def users_page(request):
    context ={
        "users": User.objects.all()
    }
    return render(request, "your_app_name_here/user.html", context)

def add_user(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        first_name = request.POST['user_first_name']
        last_name = request.POST['user_last_name']
        notes = request.POST['user_notes']
        User.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect("/users")

def add_roster(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        title = request.POST['roster_title']
        description = request.POST['roster_description']
        Roster.objects.create(title=title, description=description)
        return redirect("/")

def one_user(request, user_id):
    user = User.objects.get(id=user_id)
    this_user_rosters = user.rosters.all()
    all_rosters = Roster.objects.all()
    other_rosters = [roster for roster in all_rosters if roster not in this_user_rosters]
    context ={
        "user": user,
        "other_rosters": other_rosters,
    }
    return render(request, "your_app_name_here/view_user.html", context)

def one_roster(request, roster_id):
    roster = Roster.objects.get(id=roster_id)
    this_roster_users = roster.users.all()
    all_users = User.objects.all()
    other_users = [user for user in all_users if user not in this_roster_users]
    context = {
        "roster": roster,
        "other_users": other_users,
    }
    return render(request, "your_app_name_here/view_roster.html", context)

def add_user_to_roster(request, roster_id):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST": 
        user_id = request.POST['user_id']
        Roster.objects.get(id=roster_id).users.add(User.objects.get(id=user_id))
        return redirect(f"/rosters/{roster_id}")

def add_roster_to_user(request, user_id):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        roster_id = request.POST['roster_id']
        User.objects.get(id=user_id).rosters.add(Roster.objects.get(id=roster_id))
        return redirect(f"/users/{user_id}")