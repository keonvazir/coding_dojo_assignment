########## APP LEVEL ###############

from django.shortcuts import render

def index(request):
    return render(request, "book_user_app/index.html")
# Create your views here.
