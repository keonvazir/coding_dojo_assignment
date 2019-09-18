######### APP LEVEL views.py ###########
from django.shortcuts import render, redirect
# from django.contrib import messages

from .models import Restful

# class Restful(models.Model):
#     title = models.CharField(max_length=45)
#     network = models.CharField(max_length=45)
#     release_date = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __repr__(self):
#         return f"<Restful object: {self.id} {self.title} {self.network} {self.release_date}>"


# def root(reqeust):
#     return redirect("/shows")

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
        title = request.POST['new_title']
        network = request.POST['new_network']
        release = request.POST['new_release']
        description = request.POST['description']
        restful = Restful.objects.create(title=title, network=network, release_date = release)
        print("###################")
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
        restful = Restful.objects.get(id=restful_id)
        print("*"*80)
        restful.title = request.POST['new_title']
        restful.network = request.POST['new_network']
        restful.release_date = request.POST['new_release']
        restful.description = request.POST['description']
        restful.save()
        return redirect("/shows/"+str(restful_id))

def delete(request, restful_id):
    # if request.method == "GET":
    #     return redirect("/shows")
    # if request.method == "POST":
    delete_restful = Restful.objects.get(id=restful_id)
    delete_restful.delete()
    return redirect("/shows")