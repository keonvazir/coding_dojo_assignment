from django.shortcuts import render, HttpResponse, redirect

from .models import *

def index(request):
    context = {
        "rosters": Roster.objects.all(),
    }
    return render(request, "roster_app/index.html", context)

def add_roster(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        title = request.POST['roster_title']
        description = request.POST['roster_description']
        Roster.objects.create(title=title, description=description)
        return redirect("/")

def players_page(request):
        context = {
            "players": Player.objects.all(),

        }
        return render(request, "roster_app/player.html", context)

def one_player(request, player_id):
       player = Player.objects.get(id=player_id)
       this_player_rosters = player.rosters.all()
       all_rosters = Roster.objects.all()
       other_rosters = [roster for roster in all_rosters if roster not in this_player_rosters]
       context = {
           "player": player,
           "other_rosters": other_rosters,
       }
       return render(request, "roster_app/view_player.html", context)

def one_roster(request, roster_id):
        roster = Roster.objects.get(id=roster_id)
        this_roster_players = roster.players.all()
        all_players = Player.objects.all()
        other_players = [player for player in all_players if player not in this_roster_players]
        context = {
            "roster": roster,
            "other_players": other_players,
        }
        return render(request, "roster_app/roster.html", context)

def add_player(request):
        if request.method == "GET":
            return redirect("/")
        if request.method == "POST":
            first_name = request.POST['player_first_name']
            last_name = request.POST['player_last_name']
            notes = request.POST['player_notes']
            Player.objects.create(first_name=first_name, last_name=last_name, notes=notes)
            return redirect("/players")

def add_player_to_roster(request, roster_id):
        if request.method == "GET":
            return redirect("/")
        if request.method == "POST":
            player_id = request.POST['player_id']
            Roster.objects.get(id=roster_id).players.add(Player.objects.get(id=player_id))
            return redirect(f"/rosters/{roster_id}")
    
def add_roster_to_player(request, player_id):
        if request.method == "GET":
            return redirect("/")
        if request.method == "POST":
            roster_id = request.POST['roster_id']
            Player.objects.get(id=player_id).rosters.add(Roster.objects.get(id=roster_id))
            return redirect(f"/players/{player_id}")

    








