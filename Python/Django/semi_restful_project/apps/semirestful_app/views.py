######### APP LEVEL views.py ###########
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Restful

def root(reqeust):
    return redirect("/shows")

def index(request):
    context = {
        "all": Restful.objects.all(),
    }
    return render(request, "semirestful_app/index.html", context)

def add_new_show(request):
    context = {
        "all": Restful.objects.all(),
        
    }
    return render(request, "semirestful_app/add_new_show.html", context)

def create(request, id):
    # restfuls = Restful.objects(request.POST)
    if "count" not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    Restful.objects.create(id = request.POST['id'],title=request.POST['new_title'], network=request.POST['new_network'], release_date=request.POST['new_release'])

    restful = Restful.objects.all()

    # if request.method == "POST":
        # restful = Restful.objects.get(id=id)
        # restful.title = request.POST['new_title']
        # restful.network= request.POST['new_network']
        # restful.release_date = request.POST['new_release']
        # restful.description = request.POST['description']
        # restful.save()

        # request.session['new_title']=request.POST['new_title']
        # request.session['new_network']=request.POST['new_network']
        # request.session['new_release']=request.POST['new_release']
        # request.session['description']=request.POST['description']

    return redirect("/shows"+id)
        # return redirect("/shows"+id)

def new_show(request, id):
    context = {
        "all": Restful.objects.all(),
    }

    return render(request, "semirestful_app/new_show.html", context)

def edit(request, id):
    context = {
        "all": Restful.objects.all(),
    }

    return render(request, "semirestful_app/edit.html", context)

