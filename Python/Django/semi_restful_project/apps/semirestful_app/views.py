######### APP LEVEL views.py ###########
from django.shortcuts import render, redirect, HttpResponse
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

def create(request):
    if request.method == "GET":
        return redirect("/shows")
    if request.method == "POST":
        errors = Restful.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            # restful = Restful.objects.all()
            return redirect("/shows/new")
        else:
            title = request.POST['new_title']
            network = request.POST['new_network']
            release_date = request.POST['new_release']
            description = request.POST['description']
            
            restful = Restful.objects.create(title=title, network=network, release_date = release_date, description=description)
            
        print("#"*80)
        return redirect("/shows/"+str(restful.id))

def one_show(request, restful_id):
    restful_id = Restful.objects.get(id=restful_id)
    all_restful = Restful.objects.all()
    context = {
        "restful": restful_id
        
    }
    return render(request, "semirestful_app/one_show.html", context)

def edit_page(request, restful_id):
    restful_id = Restful.objects.get(id=restful_id)
    all_restful = Restful.objects.all()
    context = {
        "restful": restful_id
        
    }
    return render(request, "semirestful_app/edit.html", context)

def update(request, restful_id):
    if request.method == "GET":
        return redirect("/shows")
    if request.method == "POST":
        errors = Restful.objects.basic_validator(request.POST)
        if len(errors) > 0:
        # restful = Restful.objects.get(id=restful_id)
            print("*"*80)
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows"+str(restful_id)+"/edit")
        else:
            this_show = Restful.objects.get(id=restful_id)
            this_show.title = request.POST['new_title']
            this_show.network = request.POST['new_network']
            this_show.release_date = request.POST['new_release']
            this_show.description = request.POST['description']
            this_show.save()
            return redirect("/shows/"+str(restful_id)+ "/update")

def delete(request, restful_id):
    delete_restful = Restful.objects.get(id=restful_id)
    delete_restful.delete()
    return redirect("/shows")