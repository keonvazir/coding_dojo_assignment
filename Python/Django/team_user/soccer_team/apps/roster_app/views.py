from django.shortcuts import render, HttpResponse, redirect

from .models import *

def index(request):
    context = {
        "rosters": Roster.objects.all(),
    }
    return render(request, "roster_app/index.html", context)






