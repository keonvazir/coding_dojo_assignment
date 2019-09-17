####### APP LEVEL views.py ###########

from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
    return render(request, "app_ninja_gold/index.html")

def process_money(request):
    if request.method == "POST":
        if request.POST['location'] == 'farm':
            request.session['gold'] += random.randint(10, 20)
        elif request.POST['location'] == 'cave':
            request.session['gold'] += random.randint(5, 10)
        elif request.POST['location'] == 'house':
            request.session['gold'] += random.randint(2, 5)
        else:
            request.session['gold'] += random.randint(-20, 20)       
        return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")
